
from pyrep.objects.vision_sensor import VisionSensor
import numpy as np
import cv2
class Camera(VisionSensor):
    def __init__(self):
        super().__init__('camera')
        # enable camera sensor
        #self.set_explicit_handling(1)
        #self.handle_explicitly()
        # compute vision sensor intrinsic matrix
        # [ax 0  u0
        #  0  ay v0
        #  0  0  1]
        self.ax = 1/(2*np.tan(self.get_perspective_angle()/2*np.pi/180))# f/dx
        self.ay = self.ax # f/dy
        self.u0 = self.get_resolution()[0]/2 # u0
        self.v0 = self.get_resolution()[1]/2 # v0
    def capture_bgr(self):
        return cv2.cvtColor(self.capture_rgb(),cv2.COLOR_RGB2BGR)

    def uv2XYZ(self,depth_img,u,v):
        Z = depth_img[v,u]
        return Z*(u-self.u0)/self.ax, Z*(v-self.v0)/self.ay, Z