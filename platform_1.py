import pygame

BROW = (139, 69, 19)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, heigth):
        super().__init__()
        self.image = pygame.Surface((width, heigth))
        self.image.fill(BROW)
        self.rect = self.image.get_rect(topleft=(x,y))