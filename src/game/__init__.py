__author__: str = "Kjulam"

import os
import pygame
import logging
import time
from typing import Any
from game.sprites import *
from game.constants import *

start_time: float = time.time()

def get_execution_time() -> str:
    elapsed_time: float = time.time() - start_time
    elapsed_hours: str = str(int(elapsed_time // 3600)).zfill(2)
    elapsed_minutes: str = str(int(elapsed_time % 3600 // 60)).zfill(2)
    elapsed_seconds: str = str(int(elapsed_time % 60)).zfill(2)
    return f"{elapsed_hours}:{elapsed_minutes}:{elapsed_seconds}"

def mainloop(no_music: bool) -> None:
    # --------------- 初始化 --------------- #
    # ---------- 变量初始化 ---------- #
    # ----- 窗口相关变量 ----- #
    running: bool = True
    window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    logging.debug("成功创建游戏窗口")
    clock: pygame.time.Clock = pygame.time.Clock()
    frame_counter: int = 0
    score: int = 0
    can_add_score: bool = True
    game_over: bool = False
    temp: bool = True
    logging.info(f"当前分数：{score}")

    # ----- 图片 ----- #
    icon: pygame.Surface = pygame.image.load(os.path.join("assets/image", "manbo.png"))
    game_over_image: pygame.Surface = pygame.image.load(os.path.join("assets/image", "game_over.png"))

    # ----- 音乐和音效 ----- #
    background_music: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join("assets/sound", "background_music.mp3"))
    steel_tube_thud_sound: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join("assets/sound", "steel_tube_thud.wav"))
    manbo_sound: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join("assets/sound", "manbo.wav"))
    played_steel_tube_thud_sound: bool = False
    can_play_background_music: bool = True

    # ----- 字体 ----- #
    noto_sans_sc_black: pygame.font.Font = pygame.font.Font(os.path.join("assets/font", "NotoSansSC-Black.ttf"), 36)
    score_surface: pygame.Surface = noto_sans_sc_black.render(f"分数：{score}", True, WHITE)

    # ---------- 设置窗口图标 ---------- #
    pygame.display.set_icon(icon)
    logging.debug("成功设置窗口图标")

    # ---------- 角色相关 ---------- #
    # ----- 角色组 ----- #
    all_sprites: pygame.sprite.Group = pygame.sprite.Group()
    players: pygame.sprite.Group = pygame.sprite.Group()
    pillars: pygame.sprite.Group = pygame.sprite.Group()
    score_keepers: pygame.sprite.Group = pygame.sprite.Group()

    # ----- 不怎么华丽的分隔线 ----- #

    player: Player = Player()
    logging.debug("生成了新的 Player 对象")
    score_keeper: ScoreKeeper = ScoreKeeper()
    logging.debug("生成了新的 ScoreKeeper 对象")

    all_sprites.add(player)
    all_sprites.add(score_keeper)
    players.add(player)
    score_keepers.add(score_keeper)

    # --------------- 真·主循环 --------------- #
    while running:
        # ---------- 更新窗口标题 ---------- #
        pygame.display.set_caption(f"{TITLE} - 游玩时间：{get_execution_time()}")

        # ---------- ---------- ---------- #
        window.fill(BLACK)
        window.blit(score_surface, (50, 50))
        logging.debug(f"成功填充窗口背景颜色")
        clock.tick(FPS)
        logging.debug(f"成功设置帧率")

        # ---------- 背景音乐播放 ---------- #
        if not no_music:
            if can_play_background_music:
                background_music.play()
                can_play_background_music = False
            elif frame_counter % (FPS * (3 * 60 + 30)) == 0:
                can_play_background_music = True

        # ---------- 事件检测 ---------- #
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

        score_keeper_and_pillars_collided: dict[Any, list] = pygame.sprite.groupcollide(
            score_keepers,
            pillars,
            False,
            False
        )

        # ---------- 失败判定 ---------- #
        if player_and_pillars_collided:
            logging.debug("检测到玩家与柱子相撞")
            if not played_steel_tube_thud_sound:
                steel_tube_thud_sound.play()
                played_steel_tube_thud_sound = True
            window.blit(game_over_image, (35, 150))
            pygame.display.update()
            game_over = True
        else:
            played_steel_tube_thud_sound = False

        # ---------- 计分判定 ---------- #
        if score_keeper_and_pillars_collided:
            if can_add_score:
                score += 1
                logging.info(f"当前分数：{score}")
                can_add_score = False
                manbo_sound.play()
        else:
            can_add_score = True

        # ---------- 游戏窗口更新 ---------- #
        if game_over:
            if temp:
                logging.info("你撞大运喽！游戏失败")
                logging.info(f"最终得分：{score}")
                temp = False
        else:
            frame_counter += 1
            score_surface = noto_sans_sc_black.render(f"分数：{score}", True, WHITE)
            all_sprites.draw(window)
            logging.debug("成功将所有角色绘制到屏幕上")
            all_sprites.update()
            pygame.display.update()
            logging.debug("成功更新窗口")

