import os
import pygame
import game

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        player_image: pygame.Surface = pygame.image.load(os.path.join("assets/image", "manbo.png")).convert_alpha()
        self.image: pygame.Surface = pygame.transform.scale(player_image, (50, 50))                                 # 将图片设置大小为 (50, 50)
        self.mask: pygame.Mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (100, game.HEIGHT // 2)
        self.speed: int = 3

    def update(self) -> None:
        mouse_pressed: tuple = pygame.mouse.get_pressed()
        key_pressed: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        if mouse_pressed[0] or key_pressed[pygame.K_SPACE]:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > game.HEIGHT:
            self.rect.bottom = game.HEIGHT
