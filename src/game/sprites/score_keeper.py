__author__: str = "Kjulam"

import pygame

class ScoreKeeper(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((50, 50))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (50, 25)

    def update(self) -> None:
        pass
