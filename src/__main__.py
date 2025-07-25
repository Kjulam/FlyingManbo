__author__: str = "Kjulam"
__version__: str = "25.7.12"

import sys
import pygame
import logging
import argparse
import game

def main() -> int | None:
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] [%(filename)s / %(levelname)s]: %(message)s",
            datefmt="%H:%M:%S"
        )

        parser: argparse.ArgumentParser = argparse.ArgumentParser()
        parser.add_argument("-nm", "--no-music", help="关闭音乐运行", action="store_true")
        parser.add_argument("-v", "--version", help="获取游戏版本", action="store_true")
        arguments: argparse.Namespace = parser.parse_args()
        no_music: bool = arguments.no_music
        version: bool = arguments.version

        if version:
            logging.info(f"FlyingManbo version {__version__} by {__author__}")
            return 0

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
    exit_code: int | None = main()
    if exit_code is None:
        exit_code = 0
    logging.info(f"程序已退出，退出代码为 {exit_code}")
    sys.exit(exit_code)
