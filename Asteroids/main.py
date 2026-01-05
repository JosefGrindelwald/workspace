import pygame
from logger import log_state
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0
    running = True

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        log_state()

        # Clear screen
        screen.fill((0, 0, 0))  # black

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)
        dt = clock.tick()
        print(dt)

    pygame.quit()

if __name__ == "__main__":
    main()
