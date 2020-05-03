from os.path import dirname, abspath
from os import system, environ
sim_path = dirname(dirname(dirname(dirname(abspath(__file__)))))
scene_path = sim_path + '/Simulation/scene/'

import sys
sys.path.append(sim_path)
from Simulation.src.camera import Camera
from Simulation.src.env import Env
from Simulation.src.franka import Franka
from pyrep.objects.shape import Shape
import numpy as np
import cv2
import copy
environ['TF_CPP_MIN_LOG_LEVEL'] = "3" # stop print warning!!!
from DeepClaw.modules.end2end.graspNet.fc_predictor import FCPredictor

def scene(scene_file_name):
    # return abs dir of scene file 
    return scene_path + scene_file_name

def franka_move(start, target, angle):
    franka.clear_path = True
    start[2] += 0.1
    franka.move(env,start,euler=[0,np.radians(180),angle])
    start[2] -= 0.07
    franka.move(env,start,euler=[0,np.radians(180),angle])
    
    success = False
    for toy in toys:
        if franka.gripper._proximity_sensor.is_detected(toy):
            franka.grasp(env,toy)
            success = True
            break
    if not success:
        print("Fail to grasp the toy!")
    start[2] += 0.07
    franka.move(env,start,euler=[0,np.radians(180),angle])
    franka.home(env)
    a = copy.copy(franka.home_joints)
    a[0] += np.pi/2
    franka.move_j(a,env)
    franka.release(env)
    franka.home(env)

# TODO: initiate grasp predictor here, the provided model with weight has 18 classes    
# The predictor can accept the custom image size at initialization, remember to resize your image according to this shape.
# You can use the default image size.
# predictor = ...


if __name__ == '__main__':
    env = Env(scene('Claw_machine.ttt'))
    env.start()

    # franka
    franka = Franka()
    
    # cam 
    cam = Camera()

    # toys
    Bird = Shape('Bird')
    Hipp = Shape('Hipp')
    Elephant = Shape('Elephant')
    Penguin = Shape('Penguin')
    box_dest = Shape('box_dest')
    target = Shape('Sphere')
    toys = [Bird, Hipp, Elephant, Penguin]
    place_position = box_dest.get_position()

    # random exchange the position of toys
    toy_positions = [toy.get_position() for toy in toys]
    arr = np.arange(len(toys))
    np.random.shuffle(arr)
    [toys[i].set_position(toy_positions[arr[i]]) for i in range(len(toys))]

    # set franka to home joints
    franka.home(env)
    
    # TODO: complete the detection and grasp pipeline in the while loop.
    print("=========================Start picking...")
    while True:
        # TODO: capture rbg image


        # TODO: crop the image so that you only feed the region of interest to the neural network
        
        
        # TODO: resize you region of interest according to your predictor
        

        # TODO: feed the cropped image to the predictor and obtain the best grasping pixel x, y and rotation angle
        

        # TODO: compute the gasping pixel in the original image cx, cy and the success probability


        # We add a criteria to stop the simulation if the predictor fail to find 
        # any good grasp with success probability > 0.8
        if possi < 0.8:
            print("Fail to find good grasp, ending the simulation")
            break
        
        # TODO: transform u, v, z to x, y, z, you might need to set the z to 1.123 mannually for success path planning.


        # visualize the prasping point in the simulation
        target.set_position(grasp_position)
        cv2.circle(img,(cx,cy),5,(0,0,255),5)
        cv2.circle(ros,(x,y),5,(0,0,255),5)

        # move the robot to execute the grasp
        franka_move(grasp_position, place_position, angle) 

    env.stop()
    env.shutdown()
    
