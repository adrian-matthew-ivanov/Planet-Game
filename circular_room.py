import pygame
import math
import numpy as np

class CircularRoom:
    def __init__(self, pos, image:pygame.Surface, station_pos, station_angle, angle):
        self.pos = pos
        self.angle = angle
        self.image = image
        self.station_pos = station_pos
        self.station_angle = station_angle

    def draw(self, screen, camera):
        scaled_image = pygame.transform.scale(self.image, np.array(self.image.get_size())*camera.zoom)
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        screen.blit(rotated_image, (self.pos + self.station_pos)*camera.zoom - camera.pos)