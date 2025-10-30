import sys
import pygame
from settings import Settings
from ship import Ship

# Inicializa o jogo e cria um objeto para a tela
def run():  

    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    bg_color = (13, 17, 23)
    pygame.display.set_caption("Space Invaders")
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:

        # Observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # Deixa a tela mais recente visível
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run()