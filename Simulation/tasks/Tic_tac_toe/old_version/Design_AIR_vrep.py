from os.path import dirname, join, abspath
from pyrep import PyRep
from pyrep.objects.vision_sensor import VisionSensor
from pyrep.robots.arms.panda import Panda
from pyrep.robots.end_effectors.panda_gripper import PandaGripper
from pyrep.errors import ConfigurationPathError
from pyrep.const import ConfigurationPathAlgorithms as Algos
import weakref
import numpy as np
import cv2

scene_files = {
    'tic-tac-toe':'ttt.ttt'
}

class Scene(object):
    '''
    param: project_name: List[string]
    1.tic-tac-toe
    '''
    def __init__(self,project_name):
        self.SCENE_FILE = join(dirname(abspath(__file__)), scene_files[project_name])
        self.pr = PyRep()
        self.pr.launch(self.SCENE_FILE, headless=False)

    def chessboard_position(self, action):
        a = 0.06*np.array([[[-1,-1], [-1,0], [-1,1]],
                          [[0,-1],  [0,0],  [0,1]],
                          [[1,-1],  [1,0],  [1,1]]]).reshape((-1,2))[action]
        return [0.4+a[0], 0+a[1], 1.03]

    def start(self):
        self.pr.start()

    def step(self):
        self.pr.step()

    def stop(self):
        self.pr.stop()

    def shutdown(self):
        self.pr.shutdown()

class Robot():
    def __init__(self,scene):
        self.panda = Panda()
        self.PANDA_H = np.array([[1,0,0,-0.4],
                                 [0,1,0,0],
                                 [0,0,1,1],
                                 [0,0,0,1]])
        self.gripper = PandaGripper()
        self.scene_step = weakref.WeakMethod(scene.step)
        self.grasped_obj = None

    def move_p(self,position,euler=[0,np.pi,0]):
        self.panda.set_joint_positions(self.panda.get_joint_positions())
        position = np.array(position)
        print(position)
        # pos = np.append(pos,1)
        try:
            path = self.panda.get_path(
                position = position,
                euler = euler) # position = (self.PANDA_H@pos)[0:3],
        except ConfigurationPathError as e:
            print('Could not find path')
            raise e
        
        done = False
        while not done:
            done = path.step()
            self.scene_step()()
            
    def home(self):
        # 0, -M_PI_4, 0, -3 * M_PI_4, 0, M_PI_2, M_PI_4
        self.move_p([0.2, 0, 1.5],[0, np.pi, 0])

    def gripper_open(self,velocity):
        while not self.gripper.actuate(1.0,0.05):
            self.scene_step()()
        if self.grasped_obj is not None:
            self.gripper.release()
            self.grasped_obj = None
        
    def gripper_grasp(self,velocity,obj=None):
        while not self.gripper.actuate(0.0,0.05):
            self.scene_step()()
        if obj is not None:
            self.grasped_obj = obj
            self.gripper.grasp(obj)

class Camera(object):
    def __init__(self,scene):
        self.cam = VisionSensor('camera')
        # enable camera sensor
        self.cam.set_explicit_handling(1)
        self.cam.handle_explicitly()
        # compute vision sensor intrinsic matrix
        # [ax 0  u0 
        #  0  ay v0
        #  0  0  1]
        self.ax = 1/(2*np.tan(self.cam.get_perspective_angle()/2*np.pi/180))# f/dx
        self.ay = self.ax # f/dy
        self.u0 = self.cam.get_resolution()[0]/2 # u0
        self.v0 = self.cam.get_resolution()[1]/2 # v0
        self.scene_step = weakref.WeakMethod(scene.step)

    def bgr_image(self):
        for _ in range(10):
            img = self.cam.capture_rgb()
            self.scene_step()()
        return cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    def depth_image(self):
        for _ in range(10):
            depth = self.cam.capture_depth(in_meters=True)
            self.scene_step()()
        return depth

    def uv2XYZ(self,u,v):
        Z = self.depth_image()[v,u]
        return Z*(u-self.u0)/self.ax, Z*(v-self.v0)/self.ay
if __name__ == '__main__':
    a = 0.6*np.array([[[-1,-1], [-1,0], [-1,1]],
                          [[0,-1], [0,0], [0,1]],
                          [[1,-1], [1,0], [1,1]]]).reshape((-1,2))[0]
    print(a)