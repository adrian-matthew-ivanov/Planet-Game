from scene import Scene
from camera import Camera

class GameScene(Scene):
    def __init__(self, player, camera, solar_system):
        super().__init__("game")
        self.camera = camera
        self.solar_system = solar_system
        self.player = player

    def update(self, screen):
        self.player.update()
        self.solar_system.update()
        self.camera.update(screen)

    def draw(self, screen, draw_orbits=False):
        screen.fill("black")
        self.player.draw(screen, self.camera)
        self.solar_system.draw(screen, self.camera, draw_orbits)

    def get_camera(self) -> Camera:
        return self.camera