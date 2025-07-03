import pygame

import sprites
from game.constants import *

def mainloop() -> None:
    running: bool = True
    window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)

    while running:
        window.fill(BLACK)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
