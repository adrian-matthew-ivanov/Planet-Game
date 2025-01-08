from data import *

class Inventory:
    def __init__(self, size, shapes, locked_area):
        self.size = size
        self.shapes = shapes
        self.locked_area = locked_area

        self.image = inventory

    def draw_grid(screen, size, locked_area):

        for j in range(size[0]):
            pygame.draw.line(screen, "white", (j*(screen.get_width()/size[0]) + screen.get_height()//100, 0), (j*(screen.get_width()/size[0]) + screen.get_height()//100, screen.get_height()), screen.get_height()//50)

        pygame.draw.line(screen, "white", ((j+1)*(screen.get_width()/size[0]) - screen.get_height()//100, 0), ((j+1)*(screen.get_width()/size[0]) - screen.get_height()//100, screen.get_height()), screen.get_height()//50)

        for i in range(size[1]):
            pygame.draw.line(screen, "white", (0, i*(screen.get_height()/size[1]) + screen.get_height()//100), (screen.get_width(), i*(screen.get_height()/size[1]) + screen.get_height()//100), screen.get_height()//50)

        pygame.draw.line(screen, "white", (0, (i+1)*(screen.get_height()/size[1]) - screen.get_height()//100), (screen.get_width(), (i+1)*(screen.get_height()/size[1]) - screen.get_height()//100), screen.get_height()//50)

        pygame.draw.rect(screen, (51, 60, 87), ((size[0]-locked_area[0])*(screen.get_width()/size[0]) + screen.get_height()//50, (size[1]-locked_area[1])*(screen.get_height()/size[1]), locked_area[0]*(screen.get_width()/size[0]), locked_area[1]*(screen.get_height()/size[1])))

    def draw(self, screen):
        pygame.display.init()
        img = pygame.transform.scale(self.image, (screen.get_width(), screen.get_width()*(self.image.get_height()/self.image.get_width())))
        
        overlay = pygame.Surface(img.get_size())
        overlay = pygame.transform.scale(overlay, (img.get_width()*57/64, screen.get_width()*51/64*(self.image.get_height()/self.image.get_width())))
        overlay.set_colorkey("black")

        Inventory.draw_grid(overlay, self.size, self.locked_area)

        screen.blit(img, (0, screen.get_height()/2-img.get_height()/2))

        screen.blit(overlay, (img.get_width()*7/128, screen.get_height()/2-img.get_height()/2 + img.get_width()*13/128))

    