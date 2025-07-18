__author__: str = "Kjulam"

import os
import pygame
import game

class LowerPillar(pygame.sprite.Sprite):
    def __init__(self, bottom_of_corresponding_upper_pillar: int) -> None:
        super().__init__()
        pillar_image: pygame.Surface = pygame.image.load(os.path.join("assets/image", "steel_tube.png")).convert_alpha()
        self.image: pygame.Surface = pygame.transform.scale(
            pillar_image,
            (50, game.HEIGHT // 2 + 50)
        )
        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.top = bottom_of_corresponding_upper_pillar + 200
        self.rect.left = game.WIDTH
        self.speed: int = 3

    def update(self) -> None:
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
