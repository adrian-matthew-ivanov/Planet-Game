from space_object import SpaceObject
from circular_room import CircularRoom
import numpy as np
from data import stations, station_icon
import pygame
import random
import math

class SpaceStation(SpaceObject):
    def __init__(self, radius, shape, pos=np.zeros((2,)), ellipse=None, speed=0.05, follow_planet=None, rot_speed=0.02):
        super().__init__(radius, None, pos, ellipse, speed, follow_planet, "SpaceStation")
        self.shape = shape
        self.rooms = []
        self.angle = 90
        self.image = stations[self.shape]["base"]
        self.room_images = list(stations[self.shape]["rooms"].values())
        self.rot_speed = rot_speed
        self.icon_size_up = 2
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 2*self.radius, 2*self.radius)
        if self.shape == "circle":
            self.positions = [
                np.array([22, 22]),
                np.array([22, -38]),
                np.array([-7, 38]),
                np.array([-7, -45]),
                np.array([-38, 22]),
                np.array([-38, -38]),
            ]
            self.angles = [
                35, -35, 0, 0, 140, -140
            ]
            for i, position in enumerate(self.positions):
                self.rooms.append(CircularRoom(position, random.choice(self.room_images)[0], self.pos + np.array(self.rect.size)/2, self.angle, self.angles[i]))

    def update(self):
        super().update()
        if self.shape == "circle":
            self.angle += self.rot_speed
    
    def draw(self, screen, camera, draw_orbits=False, scene="game", draw_with_angle=True):
        if scene == "map":
            image = pygame.transform.scale(station_icon, np.array([station_icon.get_width()*self.icon_size_up, station_icon.get_height()*self.icon_size_up])*camera.zoom)
        elif scene == "game":
            image = pygame.transform.scale(self.image, (self.radius*2*camera.zoom, self.radius*2*camera.zoom))
        if draw_with_angle:
            rotated_image = pygame.transform.rotate(image, self.angle)
        else:
            rotated_image = image

        self.rect = pygame.Rect(self.pos[0], self.pos[1], 2*self.radius, 2*self.radius)

        screen.blit(rotated_image, self.pos*camera.zoom-camera.pos)

        if scene == "game" and self.scene_manager.get_scene_by_name("game").player.in_station:
            for room in self.rooms:
                room.station_pos = self.pos + np.array(self.rect.size)/2
                if draw_with_angle:
                    room.station_angle = self.angle
                else:
                    room.station_angle = 0
                room.draw(screen, camera)