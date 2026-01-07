import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            LINE_WIDTH
        )

    def rotate(self, direction, dt):
        # direction: +1 (links), -1 (rechts)
        self.rotation += direction * PLAYER_TURN_SPEED * dt
    def move(self, direction, dt):
        unit_vector = pygame.Vector2(0, -1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(+1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)
        if keys[pygame.K_w]:
            self.move(+1, dt)
    
