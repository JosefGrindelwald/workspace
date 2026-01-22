import pygame
import sys
from constants import *
from logger import *
from player import *
from circleshape import *
from asteroidfield import *
from sputnik import *
from UFO import *
RUNNING = "running"
GAME_OVER = "game_over"
BOSS_FIGHT = "boss_fight"
YOU_WIN = "you_win"
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)
    button_font = pygame.font.Font(None, 40)

    button_text = button_font.render("Try again", True, "black")
    button_rect = pygame.Rect(0, 0, 200, 60)
    button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    sputniks = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ufos = pygame.sprite.Group()
    def reset_game():
        nonlocal player, game_state
        for group in [asteroids, sputniks, shots, updatable, drawable]:
            group.empty()
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Shot.containers = (updatable, drawable, shots)
        Sputnik.containers = (updatable, drawable, sputniks)
        UFO.containers = (updatable, drawable, ufos)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        AsteroidField()
        ufos.empty()
        game_state = RUNNING


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Sputnik.containers = (updatable, drawable, sputniks)
    UFO.containers = (updatable, drawable, ufos)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    game_state = RUNNING
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_state == GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()
        if game_state == RUNNING:
            updatable.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player) and not player.invincible:
                    player.lives -= 1
                    player.invincible = True
                    player.invincible_timer = player.invincible_duration
                    if player.lives <= 0:
                        game_state = GAME_OVER
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        shot.kill()
                        player.get_point()
            for sputnik in sputniks:
                if sputnik.collides_with(player):
                    sputnik.kill()
                    player.lives += 1
            if player.points >= 100 and len(ufos) == 0:
                game_state = BOSS_FIGHT
                asteroid_field.kill()
                asteroids.empty()
                sputniks.empty()
                for sprite in list(asteroids):
                    sprite.kill()
                for sprite in list(sputniks):
                    sprite.kill()
                UFO(SCREEN_WIDTH // 2, 150)
        elif game_state == BOSS_FIGHT:
            updatable.update(dt)
            for ufo in ufos:
                for shot in shots:
                    if ufo.collides_with(shot):
                        shot.kill()
                        ufo.lives -= 1
                        if ufo.lives <= 0:
                            ufo.kill()
                            game_state = YOU_WIN
        screen.fill("black")
        elif game_state == YOU_WIN:
        win_text = font.render("YOU WIN!", True, "green")
        score_text = font.render(f"Final Score: {player.points}", True, "white")
        screen.blit(
            win_text,
            win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        )
        screen.blit(
            score_text,
            score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        )
        if game_state in (RUNNING, BOSS_FIGHT):
            for thing in drawable:
                thing.draw(screen)
                score_text = font.render(f"Punkte: {player.points}", True, "yellow")
                screen.blit(score_text, (10, 10))
                player.draw_lives(screen)
        if game_state == BOSS_FIGHT:
            for ufo in ufos:
                hp_text = font.render(f"UFO HP: {ufo.lives}", True, "red")
                screen.blit(hp_text, (10, 70))
        elif game_state == GAME_OVER:
            game_over_text = font.render("GAME OVER", True, "red")
            screen.blit(
                game_over_text,
                game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
            )
            pygame.draw.rect(screen, "white", button_rect)
            screen.blit(button_text, button_text.get_rect(center=button_rect.center))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
