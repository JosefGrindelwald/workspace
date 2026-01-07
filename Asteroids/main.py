import pygame
from constants import *
from logger import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    while True:
        log_state()
        updatable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in drawable:
            thing.draw(screen)

        screen.fill("black")
        pygame.display.flip()
        
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
