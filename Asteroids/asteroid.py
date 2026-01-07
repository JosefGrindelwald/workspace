import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import *

class Asteroid(CircleShape):
    image = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if Asteroid.image is None:
            Asteroid.image = pygame.image.load(
                "assets/Asteroid.png"
            ).convert_alpha()

        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-60, 60)

    def draw(self, screen):
        size = int(self.radius * 2)

        scaled_image = pygame.transform.scale(
            Asteroid.image,
            (size, size)
        )

        rotated_image = pygame.transform.rotate(
            scaled_image,
            self.rotation
        )

        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)

        for sign in (+1, -1):
            direction = self.velocity.rotate(split_angle * sign).normalize()
            position = self.position + direction * new_radius

            asteroid = Asteroid(position.x, position.y, new_radius)
            asteroid.velocity = direction * self.velocity.length() * 1.2
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt
