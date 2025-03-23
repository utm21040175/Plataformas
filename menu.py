import pygame

WHITE = (0,0,0)
BLACK = (255,255,255)

pygame.font.init()
font = pygame.font.SysFont(None, 36)

class Menu:

    def __init__(self, screen):
        self.screen = screen

    def draw_text(self, text, x, y):
        surface = font.render(text, True, BLACK)
        self.screen.blit(surface, (x,y))

    def show(self):
        menu = True

        while menu:
            self.screen.fill(WHITE)
            self.draw_text("Presiona 1 para iniciar el juego", 300, 200)
            self.draw_text("Presiona 2 para crear tu propio nivel", 300, 250)
            self.draw_text("Presiona 3 para salid", 300, 300)  
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_1:
                        menu = False
                    elif event.key == pygame.K_2:
                        print("Funcion aun no encontrada")
                    elif event.key == pygame.K_3:
                        pygame.quit()
                        exit()