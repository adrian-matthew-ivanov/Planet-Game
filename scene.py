from camera import Camera
import numpy as np

class Scene:
    def __init__(self, name):
        self.name = name

    def update(self, screen):
        pass

    def draw(self, screen):
        pass

    def get_camera(self) -> Camera:
        return Camera(np.zeros((2,)))