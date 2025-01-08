from ellipse import Ellipse
from utils import draw_ellipse_angle, draw_planet, draw_label
import numpy as np
import pygame
from scene_manager import SceneManager
import random, math

class SpaceObject:
    def __init__(self, radius:int, color:tuple, pos=np.zeros((2,)), ellipse=None, speed=0.05, follow_planet=None, type="Planet", name="None"):
        self.radius = radius
        self.color = color
        self.ellipse = ellipse
        self.pos = pos
        self.timer = 0
        self.speed = speed
        self.follow_planet = follow_planet
        self.type = type
        self.scene_manager = None
        self.name = name

        if self.type == "Planet" or self.type == "Star":
            self.alpha = 0.0 #math.radians(random.randint(0, 360))
            self.beta = -math.pi/17 #math.radians(random.randint(0, 360))
            self.gamma = -math.pi/4 #math.radians(random.randint(0, 360))
            self.image = pygame.Surface((self.radius*2, self.radius*2))
            self.map_color = (50, 230, 50)
            pos = np.array([self.radius, self.radius])
            draw_planet(self.image, self.map_color, pos, self.radius, self.alpha, self.beta, self.gamma)
            pygame.display.init()
            self.image.set_colorkey((0, 0, 0))
        
    def update(self):
        if self.ellipse != None:
            if self.follow_planet != None:
                self.ellipse.offset = self.follow_planet.pos
                self.pos = self.ellipse.get_point_pos_at_time(self.timer) + self.follow_planet.pos
            else:
                self.pos = self.ellipse.get_point_pos_at_time(self.timer)
            self.timer += self.speed

    def draw(self, display, camera, draw_orbits=False):
        if self.scene_manager.scenes[self.scene_manager.current_scene].name == "game":
            pygame.draw.circle(display, self.color, self.pos*camera.zoom-camera.pos, self.radius*camera.zoom)
            if self.ellipse != None and self.follow_planet != None and draw_orbits:
                draw_ellipse_angle(display, "white", self.ellipse.a, self.ellipse.b, self.follow_planet.pos, camera, self.ellipse.angle, 1)

        elif self.scene_manager.scenes[self.scene_manager.current_scene].name == "map":

            if camera.zoom_old != camera.zoom or self.scene_manager.old_scene != self.scene_manager.current_scene:
                map_camera=self.scene_manager.get_scene_by_name("map").get_camera()

                self.image = pygame.Surface((self.radius*2*map_camera.zoom, self.radius*2*map_camera.zoom))

                pos = np.array([self.radius, self.radius])*map_camera.zoom
                draw_planet(self.image, self.map_color, pos, self.radius*map_camera.zoom, self.alpha, self.beta, self.gamma)

                pygame.display.init()
                self.image.set_colorkey((0, 0, 0))

            display.blit(self.image, ((self.pos - np.array([self.radius, self.radius]))*camera.zoom - camera.pos))

            label_rect = draw_label(display, self.map_color, (self.pos)*camera.zoom - camera.pos, self.radius*camera.zoom, self.name)

            if label_rect.collidepoint(pygame.mouse.get_pos()):
                print("show_info " + self.name)