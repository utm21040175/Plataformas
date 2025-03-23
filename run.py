import pygame
from player import Player
from menu import Menu
from game_platform import Platform
from dialogos import DialogAnimator

pygame.init()

W, H = 1000, 600

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Juego de plataformas")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
GRAY = (200, 200, 200)

player = Player(W,H)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

platforms = pygame.sprite.Group()

levels = {
    "1":[
        [100,100,100,20],
        [200,200,100,20],
        [300,300,100,20],
        [444,444,100,20],
        [555,555,100,20],
    ],
    "2": [
        [
            50,
            50,
            100,
            100
        ],
        [
            100,
            400,
            260,
            40
        ],
        [
            680,
            340,
            140,
            60
        ],
        [
            480,
            340,
            80,
            40
        ],
        [
            380,
            280,
            20,
            20
        ],
        [
            320,
            240,
            20,
            20
        ],
        [
            240,
            200,
            40,
            20
        ],
        [
            440,
            120,
            60,
            20
        ],
        [
            360,
            40,
            20,
            40
        ]
    ],
    "3": [[50, 50, 100, 100], [300, 140, 400, 10], [120, 560, 760, 40], [320, 420, 340, 60], [840, 160, 80, 200], [40, 160, 200, 180], [520, 40, 100, 60], [440, 60, 20, 60], [740, 340, 60, 40], [760, 240, 40, 40], [260, 240, 20, 80]],
    "4": [
        [
            50,
            50,
            100,
            100
        ],
        [
            140,
            480,
            140,
            20
        ],
        [
            620,
            480,
            200,
            20
        ],
        [
            400,
            400,
            120,
            20
        ],
        [
            240,
            320,
            60,
            40
        ],
        [
            680,
            300,
            80,
            40
        ],
        [
            280,
            180,
            20,
            40
        ],
        [
            680,
            220,
            20,
            40
        ],
        [
            380,
            220,
            120,
            40
        ],
        [
            620,
            140,
            20,
            20
        ],
        [
            460,
            140,
            20,
            20
        ],
        [
            540,
            60,
            20,
            20
        ],
        [
            420,
            20,
            40,
            20
        ]
    ],
    "5": [
        [
            50,
            50,
            100,
            100
        ],
        [
            60,
            260,
            300,
            80
        ],
        [
            560,
            240,
            220,
            40
        ],
        [
            500,
            140,
            140,
            40
        ],
        [
            420,
            300,
            120,
            100
        ],
        [
            680,
            500,
            160,
            40
        ],
        [
            440,
            480,
            100,
            60
        ],
        [
            180,
            400,
            200,
            60
        ]
    ]
}

current_level = 1
max_levels = len(levels)

level_dialogs = {
    1: ["¡Bienvenido al nivel 1!", "Usa las flechas para moverte y espacio para saltar.", "Llega a la parte superior de la pantalla para avanzar al siguiente nivel."],
    2: ["¡Has alcanzado el nivel 2!", "Este nivel es más difícil.", "Sigue subiendo para llegar al último nivel."],
    3: ["¡Has alcanzado el nivel 3!", "Buena suerte y no lo olvides...", "Sigue subiendo para llegar al último nivel."],
    4: ["¡Has alcanzado el nivel 4!", "Ya casi.", "Sigue subiendo para llegar al último nivel."],
    5: ["¡Nivel final!", "¡Buena suerte!", "Completa este nivel para ganar el juego."]
}

try:
    dialog_system = DialogAnimator(level_dialogs[current_level], "burbuja.jpeg")
    show_dialog = True
except:
    dialog_system = None
    show_dialog = False
    print("No se encontro toda la informacion del dialogo")

def load_level(level_number):
    global current_level, dialog_system, show_dialog

    if str(level_number) not in levels:
        print("Has completado todos los niveles")
        return False
    
    for sprite in platforms:
        sprite.kill()

    for tp in levels[str(level_number)]:
        plat = Platform(tp[0], tp[1], tp[2], tp[3])
        platforms.add(plat)
        all_sprites.add(plat)

    platform_width = W - 500

    base_platform = Platform((W - platform_width) // 2, H - 20, platform_width, 20)
    platforms.add(base_platform)
    all_sprites.add(base_platform)

    player.rect.x = W //2
    player.rect.y = H - 100
    player.vel_y = 0

    current_level = level_number

    if level_number in level_dialogs and dialog_system is not None:
        dialog_system.textos = level_dialogs[level_number]
        dialog_system.texto_actual_indice = 0
        dialog_system.texto_actual = ""
        dialog_system.textos_finalizo = False
        show_dialog = True
    else:
        show_dialog = False

    return True

load_level(1)

Menu(screen).show()

font = pygame.font.Font(None, 36)

running = True
game_paused = False
game_completed = False

while running: 
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_paused:
                player.jump()
            elif event.key == pygame.K_RETURN and show_dialog:
                if dialog_system.textos_finalizo:
                    dialog_system.texto_actual_indice += 1
                    dialog_system.texto_actual = ""
                    dialog_system.textos_finalizo = False
                    if dialog_system.texto_actual_indice >= len(dialog_system.textos):
                        show_dialog = False
                        game_paused = False
            elif event.key == pygame.K_r and game_completed:
                current_level = 1
                game_completed = False
                load_level(1)
    if not game_paused and not game_completed:
        keys = pygame.key.get_pressed()
        player.vel_x = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT])*5
        
        all_sprites.update(platforms)
        if player.rect.top > H:
            print("PERDISTE JAJAJA ")
            player.rect.x = W//2
            player.rect.y = H - 100
            player.vel_y = 0
        if player.rect.top < 10:
            next_level = current_level + 1
            if next_level > max_levels:
                print("HAS COMPLETADO TODOS LOS NIVELES")
                game_completed = True
            else: 
                if load_level(next_level):
                    print("AVANZASTE DE NIVEL")
                else: 
                    game_completed = True
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    if show_dialog and dialog_system is not None:
        game_paused = True
        pygame.draw.rect(screen, GRAY, (0,H-150, W,150))
        
        if dialog_system.texto_actual_indice < len(dialog_system.textos):
            current_full_text = dialog_system.textos[dialog_system.texto_actual_indice]
            dialog_system.typing(current_full_text)
            text_surface = font.render(dialog_system.texto_actual, True, BLACK)
            screen.blit(text_surface, (50, H - 100))
            if hasattr(dialog_system, "avatar"):
                screen.blit(dialog_system.avatar, (W -350, H -400))
            if dialog_system.textos_finalizo:
                continue_text = font.render("PRESIONA ENTER PARA CONTINUAR", True, BLACK)
                screen.blit(continue_text, (W-400, H-50))

    if game_completed:
        overlay = pygame.Surface((W,H), pygame.SRCALPHA)
        overlay.fill((0,0,0,128))
        screen.blit(overlay, (0,0))
        
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("JUEGO COMPLETADO", True, WHITE)
        restart_text = font.render("PRESIONA R PARA REINICIAR", True, WHITE)
        
        screen.blit(game_over_text, (W //2 - game_over_text.get_width()//2, H // 2 - 50))
        screen.blit(restart_text, (W //2 - restart_text.get_width()//2, H // 2 + 50))
    
    pygame.display.flip()

pygame.quit()