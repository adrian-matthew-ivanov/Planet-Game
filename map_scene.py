from scene import Scene
from camera import Camera
import pygame
from data import ui

class MapScene(Scene):
    def __init__(self, player, camera:Camera, solar_system):
        super().__init__("map")
        self.player = player
        self.camera = camera
        self.solar_system = solar_system

    def update(self, screen):
        self.player.update(False)
        self.camera.update(screen)
        self.solar_system.update()

    def draw(self, screen, draw_orbits=False):
        screen.fill("black")
        if self.player.in_station:
            screen.blit(ui["pointer_down"], (self.solar_system.station.rect.centerx*self.camera.zoom - self.camera.pos[0], (self.solar_system.station.pos[1]-5)*self.camera.zoom - self.camera.pos[1]))
        else:
            pygame.draw.circle(screen, "white", self.player.pos*self.camera.zoom - self.camera.pos, 5)

        self.solar_system.draw(screen, self.camera, draw_orbits, scene="map")

    def get_camera(self) -> Camera:
        return self.camera