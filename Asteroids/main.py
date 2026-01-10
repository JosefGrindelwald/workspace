import pygame
import sys
from constants import *
from logger import *
from player import *
from circleshape import *
from asteroidfield import *
from sputnik import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font(None, 32)
    screen.fill("black")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    sputniks = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Sputnik.containers = (updatable, drawable, sputniks)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        updatable.update(dt)
        if thing.collides_with(player):
            log_event("player_hit")
            if player.lives > 0:
                player.lives -= 1
                print(f"Leben verloren! Noch {player.lives} Leben")
                player.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            else:
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    player.get_point()
        for thing in sputniks:
            if thing.collides_with(player):
                thing.kill()
                player.level_up()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        score_text = font.render(f"Punkte: {player.points}", True, "yellow")
        screen.blit(score_text, (10, 10))
        player.draw_lives(screen)
        pygame.display.flip()
        
        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
