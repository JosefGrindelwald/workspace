
import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    image = None
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        if Player.image is None:
            Player.image = pygame.image.load(
                "assets/Spaceship.png"
            ).convert_alpha()

        self.rotation = 0
        self.cooldown = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS


    def draw(self, screen):
        size = int(self.radius * 2)
        scaled_image = pygame.transform.scale(
            Player.image,
            (size, size)
        )
        rotated_image = pygame.transform.rotate(
            scaled_image,
            self.rotation 
        )
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * direction * dt
    def shoot(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot_position = self.position + forward * (self.radius + 5)
        Shot(shot_position.x, shot_position.y, forward)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt  # Cooldown runterzählen

        if keys[pygame.K_a]:
            self.rotate(+1, dt)
        if keys[pygame.K_d]:
            self.rotate(-1, dt)
        if keys[pygame.K_w]:
            self.move(+1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)

        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
            self.cooldown = self.shoot_cooldown
    
