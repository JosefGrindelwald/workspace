import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOOT_SPEED
        self.owner = owner

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "red",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
