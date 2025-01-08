from data import *
import numpy as np
import pygame
import math

from scene_manager import SceneManager
from space_station import SpaceStation
from solar_system import SolarSystem

class Player:
    def __init__(self, pos, solar_system:SolarSystem, scene_manager:SceneManager, in_station=False, station=SpaceStation(0, "circle")):
        self.current_ship_index = 0
        self.pos = pos
        self.vel = np.zeros((2,))
        self.image = ships[self.current_ship_index]
        self.size_down_amount = 3
        self.rotation_velocity = 0
        self.angle = 0
        self.keys = {
            "Up": False,
            "Down": False,
            "Left": False,
            "Right": False,
            "Space": False
        }
        self.speed = 0
        self.accelleration = 0.02
        self.max_speed = 0.1
        self.in_station = in_station
        self.station = station
        self.solar_system = solar_system
        self.scene_manager = scene_manager
        self.rect = None

    def update(self, do_key_updates=True):
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width()/self.size_down_amount, self.image.get_height()/self.size_down_amount)
        camera = self.scene_manager.get_scene_current_scene().get_camera()
        self.station.update()
        if self.in_station:
            if self.scene_manager.get_scene_current_scene().name == "game":
                camera.set_zoom(camera.actual_zoom)
            self.pos = self.station.pos + np.array(self.station.rect.size)/2 - np.array(self.rect.size)/2
            if self.keys["Space"]:
                self.scene_manager.get_scene_by_name("game").solar_system.station_has_player = False
                self.in_station = False
        else:
            if self.scene_manager.get_scene_current_scene().name == "game":
                dist_to_station = math.dist(self.rect.center, self.solar_system.station.rect.center)
                if dist_to_station < 2*self.station.radius:
                    camera.set_zoom(2*camera.actual_zoom)
                    if dist_to_station < self.station.radius:
                        if self.keys["Space"]:
                            self.scene_manager.get_scene_by_name("game").solar_system.station_has_player = True
                            self.in_station = True
                            self.vel = np.zeros((2,))
                            self.rect.centerx = self.station.rect.centerx
                            self.rect.centery = self.station.rect.centery
                            self.pos = np.array([float(self.rect.x), float(self.rect.y)])
                else:
                    camera.set_zoom(camera.actual_zoom)

            self.pos += self.vel
            self.rotation_velocity *= 0.95
            if do_key_updates:
                if self.keys["Right"]:
                    self.rotation_velocity -= 0.3

                if self.keys["Left"]:
                    self.rotation_velocity += 0.3

                if self.keys["Up"]:
                    self.speed += self.accelleration

                if self.keys["Down"]:
                    self.speed -= self.accelleration

            self.angle += self.rotation_velocity
            if self.speed != 0:
                self.speed = np.clip(self.speed, -1 * self.max_speed, self.max_speed)
                if abs(self.speed) <= 0.000000000001:
                    self.speed = 0
            self.speed *= 0.1
            
            self.vel[0] += math.cos(-math.radians(self.angle)) * self.speed
            self.vel[1] += math.sin(-math.radians(self.angle)) * self.speed
            

    def draw(self, display, camera):
        display_image = pygame.transform.scale(self.image, np.array(self.image.get_size())*camera.zoom/self.size_down_amount)
        display_image = pygame.transform.rotate(display_image, self.angle)
        #pygame.draw.rect(display, "green", [self.rect.x * camera.zoom - camera.pos[0], self.rect.y * camera.zoom - camera.pos[1], self.rect.width*camera.zoom, self.rect.height*camera.zoom])
        display.blit(display_image, self.pos*camera.zoom-camera.pos)