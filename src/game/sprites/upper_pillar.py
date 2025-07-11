__author__: str = "Kjulam"

import os
import pygame
import random
import game

class UpperPillar(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        pillar_image: pygame.Surface = pygame.image.load(os.path.join("assets/image", "steel_tube.png")).convert_alpha()
        rotated_pillar_image: pygame.Surface = pygame.transform.rotate(pillar_image, 180)                           # 将图片旋转 180 度，即上下颠倒
        self.image: pygame.Surface = pygame.transform.scale(
            rotated_pillar_image,
            (50, game.HEIGHT // 2 + 50)
        )
        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.bottom = random.randint(50, game.HEIGHT // 2 + 50)
        self.rect.left = game.WIDTH
        self.speed: int = 3

    def get_rect_bottom(self) -> int:
        return self.rect.bottom

    def update(self) -> None:
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
