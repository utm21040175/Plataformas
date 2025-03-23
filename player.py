import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.image = pygame.image.load("burbuja.jpeg")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT-100)
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5
        self.jump_strength = -14
        self.on_ground = False

    def update(self, platforms):
        self.vel_y += self.gravity
        
        if self.vel_y > 10:
            self.vel_y = 10
        
        self.rect.x += self.vel_x

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0 and self.rect.right > platform.rect.left and self.rect.left < platform.rect.left:
                    self.rect.right = platform.rect.left

                elif self.vel_x < 0 and self.rect.left < platform.rect.right and self.rect.right > platform.rect.right:
                    self.rect.left = platform.rect.right

        self.rect.y += self.vel_y
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0 and self.rect.bottom > platform.rect.top and self.rect.top < platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

                elif self.vel_y < 0 and self.rect.top < platform.rect.bottom and self.rect.bottom > platform.rect.bottom:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False


