import numpy as np

class Camera:
    def __init__(self, pos, offset=np.zeros((2,)), zoom=1, follow_player=None):
        self.pos = pos.astype(np.float64)
        self.offset = offset
        self.movement = {
            "Up": False,
            "Down": False,
            "Left": False,
            "Right": False
        }
        self.zoom = zoom
        self.actual_zoom = zoom
        self.zoom_old = zoom
        self.speed = 5
        self.original_speed = 5
        self.follow_player = follow_player

    def update(self, screen):
        if self.follow_player == None:
            self.pos[0] += (self.movement["Right"] - self.movement["Left"])*self.speed
            self.pos[1] += (self.movement["Down"] - self.movement["Up"])*self.speed

        else:
            self.pos = (self.follow_player.pos - self.offset)*self.zoom
            self.offset = (np.array(screen.get_size())/2-np.array(self.follow_player.image.get_size())/2)/self.zoom

    def set_zoom(self, zoom):
        self.offset *= self.zoom
        self.zoom = zoom
        self.offset /= self.zoom