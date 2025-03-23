import pygame

BROWN = (139, 69, 19)

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect(topleft=(x,y))
        