import sys
import pygame

import game

def main() -> int:
    try:
        pygame.init()
        game.mainloop()
        pygame.quit()
    except KeyboardInterrupt:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
