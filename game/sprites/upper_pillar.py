import pygame
import random
import game

class UpperPillar(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((50, game.HEIGHT // 2 + 50))
        self.image.fill(game.BLUE)
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
