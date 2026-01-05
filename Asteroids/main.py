import pygame
from logger import log_state
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        log_state()
        "black".fill
        display.flip()
    print("Starting Asteroids with pygame version: VERSION")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()
