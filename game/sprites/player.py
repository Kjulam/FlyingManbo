import pygame

import game

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((50, 25))
        self.image.fill(game.GREEN)
        self.rect: pygame.Rect = pygame
