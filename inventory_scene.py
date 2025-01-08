from scene import Scene
from inventory import Inventory
import pygame
import numpy as np

class InventoryScene(Scene):
    def __init__(self):
        super().__init__(name="InventoryScene")
        self.current_units = []

        self.inventory = Inventory(np.array([7, 3]), [],  np.array([3, 3]))
        
        self.inventory_display = pygame.Surface((400, 600))

    def update(self, screen):
        self.inventory_display = pygame.transform.scale(self.inventory_display, (screen.get_width()/2, screen.get_height()))

    def draw(self, screen):
        self.inventory_display.fill("black")
        self.inventory.draw(self.inventory_display)

        screen.blit(self.inventory_display, (0, 0))