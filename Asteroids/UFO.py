import pygame
from circleshape import *
from constants import *
from shot import *
import os
class UFO(CircleShape):
    image = None

    def __init__(self, x, y):
        super().__init__(x, y, radius=40)

        if UFO.image is None:
            UFO.image = pygame.image.load("assets/UFO.png").convert_alpha()

        self.rotation = 0
        self.rotation_speed = 100
        self.velocity = pygame.Vector2(0, 0)

        self.lives = 100
        self.shoot_cooldown = 0.2
        self.shoot_timer = 0

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        angles = [ -10, 0, 10 ]

        for angle in angles:
                dir = forward.rotate(angle)
                pos = self.position + dir * self.radius
                Shot(pos.x, pos.y, dir, owner="UFO")

    def update(self, dt):
        self.rotation += self.rotation_speed * dt
        self.shoot_timer -= dt

        if self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = self.shoot_cooldown

    def draw(self, screen):
        size = int(self.radius * 2)
        scaled_image = pygame.transform.scale(
            UFO.image,
            (size, size)
        )
        rotated_image = pygame.transform.rotate(
            scaled_image,
            -self.rotation 
        )
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)
