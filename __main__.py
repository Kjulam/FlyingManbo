__author__: str = "Kjulam"

import sys
import pygame
import logging
import argparse
import game

def main() -> int:
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] [%(filename)s / %(levelname)s]: %(message)s",
            datefmt="%H:%M:%S"
        )

        parser: argparse.ArgumentParser = argparse.ArgumentParser()
        parser.add_argument("-nm", "--no-music", help="关闭音乐运行", action="store_true")
        args: argparse.Namespace = parser.parse_args()
        no_music: bool = args.no_music

        pygame.init()
        pygame.mixer.init()
        logging.info("Pygame 初始化成功")
        game.mainloop(no_music)
        pygame.quit()

    except KeyboardInterrupt:
        logging.critical("KeyboardInterrupt")
        return -1

    except Exception as e:
        logging.error(f"发生错误：{repr(e)}")
        return 1

    logging.info("游戏正常退出")
    return 0

if __name__ == '__main__':
    sys.exit(main())
