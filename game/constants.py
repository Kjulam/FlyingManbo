import os
import pygame

# 颜色常量
BLACK: str = "#000000"
WHITE: str = "#FFFFFF"
GREEN: str = "#00FF00"
BLUE: str = "#0000FF"

# 窗口相关
WIDTH: int = 800
HEIGHT: int = 600
FPS: int = 60
TITLE: str = "飞翔的小鸟"
ICON: pygame.Surface = pygame.image.load(os.path.join("assets/image", "icon.ico"))
