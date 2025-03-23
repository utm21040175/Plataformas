import pygame

class DialogAnimator:
    def __init__(self, textos, avatar):
        self.avatar = pygame.image.load(avatar)
        self.avatar = pygame.transform.scale(self.avatar, (300, 300))
        self.textos = textos
        self.texto_actual_indice = 0
        self.texto_actual = ""
        self.velocidad_text = 3
        self.tiempo_texto = 0
        self.textos_finalizo = False

    def typing(self, texto_completo):
        if len(self.texto_actual)  < len(texto_completo):
            self.texto_actual += texto_completo[len(self.texto_actual)]
        else:
            self.textos_finalizo = True

    def shake(self):
        shake_offset = pygame.math.Vector2(0,0)
        shake_offset.x = pygame.math.lerp(-5, 5, pygame.time.get_ticks()%100/100)
        self.textos_finalizo = True
        return shake_offset