# Made by Prygin

import pygame, sys
import random, math
from data import *
from utils import generate_star_name
import numpy as np

# Import Objects
from space_object import SpaceObject #DELETE
from ellipse import Ellipse #DELETE

from space_station import SpaceStation
from player import Player
from camera import Camera
from solar_system import SolarSystem
from scene_manager import SceneManager

# Scenes
from map_scene import MapScene
from game_scene import GameScene
from inventory_scene import InventoryScene

pygame.init()
pygame.font.init()

resize_ratio = 1
width = 800
height = 600

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Planet Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial Bold', 20)

draw_orbits = False

map_camera = Camera(np.array([0, 0]), np.array([screen.get_width()/2, screen.get_height()/2]))

solar_system = SolarSystem(np.zeros((2,)), generate_star_name(), 5, 500, (1, 50), scene_manager=None, planets=[ #DELETE
     SpaceObject(60, (63,84,186), ellipse=Ellipse(1500, 1200, 0), type="Planet", speed=0.00005), #DELETE
], station=SpaceStation(60, "circle", ellipse=Ellipse(800, 600, 0.3*math.pi), speed=0.00005, rot_speed=0.02), #DELETE
station_has_player=True)
solar_system.update()

player = Player(pos=np.zeros((2,)), in_station=True, station=solar_system.station, solar_system=solar_system, scene_manager=None)
game_zoom = 5
game_camera = Camera(np.array([0, 0]), zoom=game_zoom, follow_player=player, offset=(np.array(screen.get_size())/2-np.array(player.image.get_size())/2)/game_zoom)

scene_manager = SceneManager([MapScene(player, map_camera, solar_system), GameScene(player, game_camera, solar_system), InventoryScene()], 2)

player.scene_manager = scene_manager
solar_system.scene_manager = scene_manager

while True:
    current_scene = scene_manager.get_scene_current_scene()
    map_camera.zoom_old = map_camera.zoom

    player.keys["Space"] = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                map_camera.movement["Up"] = True
                player.keys["Up"] = True

            if event.key == pygame.K_s:
                map_camera.movement["Down"] = True
                player.keys["Down"] = True

            if event.key == pygame.K_a:
                map_camera.movement["Left"] = True
                player.keys["Left"] = True

            if event.key == pygame.K_d:
                map_camera.movement["Right"] = True
                player.keys["Right"] = True

            if event.key == pygame.K_SPACE:
                player.keys["Space"] = True

            if event.key == pygame.K_t:
                player.vel = np.zeros([2,])
                player.speed = 0
            if event.key == pygame.K_m:

                if current_scene.name == "game":
                    scene_manager.set_scene_by_name("map")
                elif current_scene.name == "map":
                    scene_manager.set_scene_by_name("game")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                map_camera.movement["Up"] = False
                player.keys["Up"] = False

            if event.key == pygame.K_s:
                map_camera.movement["Down"] = False
                player.keys["Down"] = False

            if event.key == pygame.K_a:
                map_camera.movement["Left"] = False
                player.keys["Left"] = False

            if event.key == pygame.K_d:
                map_camera.movement["Right"] = False
                player.keys["Right"] = False

        if current_scene.name == "map":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    if map_camera.zoom <= 6.1:
                        scene_manager.get_scene_by_name("map").get_camera().zoom *= 1.1

                if event.button == 5:
                    if map_camera.zoom >= 0.2:
                        scene_manager.get_scene_by_name("map").get_camera().zoom /= 1.1
    
    current_scene.update(screen)
    current_scene.draw(screen)

    # Update handling

    pygame.display.update()
    clock.tick(60)

    scene_manager.old_scene = scene_manager.current_scene