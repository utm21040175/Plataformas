import pygame

# Clase del jugador que hereda de pygame.sprite.Sprite para usar sprites
class Player2(pygame.sprite.Sprite):

    def __init__(self, WIDTH, HEIGHT):
        super().__init__()  # Llama al constructor de la clase base
        # Cargar la imagen del jugador, redimensionarla y obtener su rectángulo
        self.image = pygame.image.load("burbuja.jpeg")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # Centrar el rectángulo en el ancho y a cierta distancia desde el fondo
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        # Inicializar las velocidades en x e y
        self.vel_x = 0
        self.vel_y = 0
        # Gravedad para que el personaje caiga
        self.gravity = 0.5
        # Fuerza del salto
        self.jump_strength = -14
        # Variable para saber si el jugador está en el suelo
        self.on_ground = False

    # Actualizar el estado del jugador
    def update(self, platforms):
        # Aplicar la gravedad
        self.vel_y += self.gravity

        # Limitar la velocidad máxima de caída
        if self.vel_y > 10:
            self.vel_y = 10

        # Actualizar la posición horizontal
        self.rect.x += self.vel_x

        # Manejar colisiones horizontales con plataformas
        for platform in platforms:
            if self.rect.colliderect(platform.rect):  # Si hay colisión
                # Si el jugador se mueve hacia la derecha
                if self.vel_x > 0 and self.rect.right > platform.rect.left and self.rect.left < platform.rect.left:
                    self.rect.right = platform.rect.left  # Detenerlo en el borde izquierdo de la plataforma

                # Si el jugador se mueve hacia la izquierda
                elif self.vel_x < 0 and self.rect.left < platform.rect.right and self.rect.right > platform.rect.right:
                    self.rect.left = platform.rect.right  # Detenerlo en el borde derecho de la plataforma

        # Actualizar la posición vertical
        self.rect.y += self.vel_y
        self.on_ground = False  # Por defecto, asumimos que el jugador está en el aire

        # Manejar colisiones verticales con plataformas
        for platform in platforms:
            if self.rect.colliderect(platform.rect):  # Si hay colisión
                # Si el jugador está cayendo y colisiona con la parte superior de la plataforma
                if self.vel_y > 0 and self.rect.bottom > platform.rect.top and self.rect.top < platform.rect.top:
                    self.rect.bottom = platform.rect.top  # Detenerlo en la parte superior de la plataforma
                    self.vel_y = 0  # Detener el movimiento vertical
                    self.on_ground = True  # El jugador está en el suelo

                # Si el jugador está subiendo y colisiona con la parte inferior de la plataforma
                elif self.vel_y < 0 and self.rect.top < platform.rect.bottom and self.rect.bottom > platform.rect.bottom:
                    self.rect.top = platform.rect.bottom  # Detenerlo en la parte inferior de la plataforma
                    self.vel_y = 0  # Detener el movimiento vertical

    # Método para que el jugador salte
    def jump(self):
        if self.on_ground:  # Solo puede saltar si está en el suelo
            self.vel_y = self.jump_strength  # Aplicar la fuerza del salto
            self.on_ground = False  # Ahora está en el aire
