import pygame
import random
from circleshape import *
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for _ in range(2):
                angle = random.uniform(20, 50)  
                direction = pygame.Vector2(0, -1).rotate(angle)
                position = self.position + direction * new_radius
                asteroid = Asteroid(position.x, position.y, new_radius)
                asteroid.velocity = direction * self.velocity.length() * 1.2
    def update(self, dt):
        self.position += self.velocity * dt
