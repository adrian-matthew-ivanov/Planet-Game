from utils import rotate
import numpy as np
import math

class Ellipse:
    def __init__(self, a:float, b:float, angle:float):
        self.a = a
        self.b = b
        self.angle = angle

    def get_point_pos_at_time(self, time):
        return rotate(np.array([self.a*math.cos(time), self.b*math.sin(time)]), self.angle)