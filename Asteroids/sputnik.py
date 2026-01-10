import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import *

class Sputnik(CircleShape):
    image = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if Sputnik.image is None:
            Sputnik.image = pygame.image.load(
                "assets/Sputnik.png"
            ).convert_alpha()

        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-60, 60)

    def draw(self, screen):
        size = int(self.radius * 2)

        scaled_image = pygame.transform.scale(
            Sputnik.image,
            (size, size)
        )

        rotated_image = pygame.transform.rotate(
            scaled_image,
            self.rotation
        )

        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)
     def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt
