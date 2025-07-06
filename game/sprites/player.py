import pygame
import game

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((50, 30))
        self.image.fill(game.GREEN)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (100, game.HEIGHT // 2)
        self.speed: int = 3

    def update(self) -> None:
        mouse_pressed: tuple = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > game.HEIGHT:
            self.rect.bottom = game.HEIGHT
