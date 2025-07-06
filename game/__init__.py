import pygame
import logging
from game.sprites import *
from game.constants import *

def mainloop() -> None:
    running: bool = True
    window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    logging.debug("成功创建游戏窗口")
    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)
    logging.debug(f"成功设置窗口标题为 \"{TITLE}\"")
    frame_counter: int = 0

    all_sprites: pygame.sprite.Group = pygame.sprite.Group()
    pillars: pygame.sprite.Group = pygame.sprite.Group()

    player: Player = Player()
    logging.debug("生成了新的 Player 对象")

    all_sprites.add(player)

    while running:
        window.fill(BLACK)
        logging.debug(f"成功填充窗口背景颜色")
        clock.tick(FPS)
        logging.debug(f"成功设置帧率")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.debug("检测到游戏事件：pygame.QUIT")
                running = False

            if event.type == pygame.KEYUP:
                logging.debug("检测到游戏事件：pygame.KEYUP")
                if event.key == pygame.K_ESCAPE:
                    logging.debug("按下的键是：Escape")
                    running = False

        if frame_counter % (FPS * 2) == 0:
            upper_pillar: UpperPillar = UpperPillar()
            logging.debug("生成了新的 UpperPillar 对象")
            lower_pillar: LowerPillar = LowerPillar(upper_pillar.get_rect_bottom())
            logging.debug("生成了新的 LowerPillar 对象")
            all_sprites.add(upper_pillar)
            all_sprites.add(lower_pillar)
            pillars.add(upper_pillar)
            pillars.add(lower_pillar)

        frame_counter += 1
        all_sprites.draw(window)
        logging.debug("成功将所有角色绘制到屏幕上")
        all_sprites.update()
        pygame.display.update()
        logging.debug("成功更新窗口")
