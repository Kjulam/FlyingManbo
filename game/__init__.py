import os
import pygame
import logging
from typing import Any
from game.sprites import *
from game.constants import *

def mainloop() -> None:
    # --------------- 初始化 --------------- #
    # ---------- 变量初始化 ---------- #
    # ----- 窗口相关变量 ----- #
    running: bool = True
    window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    logging.debug("成功创建游戏窗口")
    clock: pygame.time.Clock = pygame.time.Clock()
    frame_counter: int = 0
    # ----- 音效 ----- #
    steel_tube_thud_sound: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join("assets/sound", "steel_tube_thud.wav"))
    played_steel_tube_thud_sound: bool = False

    # ---------- 设置窗口标题和图标 ---------- #
    pygame.display.set_caption(TITLE)
    logging.debug(f"成功设置窗口标题为 \"{TITLE}\"")
    pygame.display.set_icon(ICON)
    logging.debug("成功设置窗口图标")

    # ---------- 角色相关 ---------- #
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()
    players: pygame.sprite.Group = pygame.sprite.Group()
    pillars: pygame.sprite.Group = pygame.sprite.Group()

    player: Player = Player()
    logging.debug("生成了新的 Player 对象")

    all_sprites.add(player)
    players.add(player)

    # --------------- 真·主循环 --------------- #
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

        # ---------- 柱子的生成 ---------- #
        if frame_counter % (FPS * 2) == 0:
            upper_pillar: UpperPillar = UpperPillar()
            logging.debug("生成了新的 UpperPillar 对象")
            lower_pillar: LowerPillar = LowerPillar(upper_pillar.get_rect_bottom())
            logging.debug("生成了新的 LowerPillar 对象")
            all_sprites.add(upper_pillar)
            all_sprites.add(lower_pillar)
            pillars.add(upper_pillar)
            pillars.add(lower_pillar)

        # ---------- 角色的碰撞 ---------- #
        player_and_pillars_collided: dict[Any, list] = pygame.sprite.groupcollide(
            players,
            pillars,
            False,
            False,
            collided=pygame.sprite.collide_mask
        )

        if player_and_pillars_collided:
            logging.debug("检测到玩家与柱子相撞")
            if not played_steel_tube_thud_sound:
                steel_tube_thud_sound.play()
                played_steel_tube_thud_sound = True

        else:
            played_steel_tube_thud_sound = False

        # ---------- 游戏窗口更新 ---------- #
        frame_counter += 1
        all_sprites.draw(window)
        logging.debug("成功将所有角色绘制到屏幕上")
        all_sprites.update()
        pygame.display.update()
        logging.debug("成功更新窗口")
