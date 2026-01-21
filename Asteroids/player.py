
import pygame
from circleshape import *
from constants import *
from shot import *
import os



class Player(CircleShape):
    image = None
    heart_image = None
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        if Player.image is None:
            Player.image = pygame.image.load(
                "assets/Spaceship.png"
            ).convert_alpha()
        if Player.heart_image is None:
            Player.heart_image = pygame.image.load(
                "assets/Heart.png"
            ).convert_alpha()

        self.rotation = 0
        self.cooldown = 0
        self.level = 1
        self.points = 0
        self.lives = 1  
        self.next_life_threshold = 10
        self.base_shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.fire_mode = "single"   
        self.cooldown_bonus = False
        self.invincible = False
        self.invincible_timer = 0.0
        self.invincible_duration = 1.0 

    def draw(self, screen):
        size = int(self.radius * 4)
        scaled_image = pygame.transform.scale(
            Player.image,
            (size, size)
        )
        rotated_image = pygame.transform.rotate(
            scaled_image,
            -self.rotation 
        )
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)
    def draw_lives(self, screen):
        heart_size = 24  # Größe jedes Herz-Icons (px)
        spacing = 5      # Abstand zwischen den Herzen
        x = 10
        y = 40  # direkt unter Score
        for i in range(self.lives):
            heart = pygame.transform.scale(Player.heart_image, (heart_size, heart_size))
            screen.blit(heart, (x + i * (heart_size + spacing), y))

    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * direction * dt
    def get_point(self):
        self.points += 1
    def level_up(self):
        self.level += 1
        if self.level == 2 and not self.cooldown_bonus:
            self.base_shoot_cooldown *= 0.8
            self.cooldown_bonus = True
        elif self.level == 3:
            self.fire_mode = "double"
        elif self.level == 4:
            self.fire_mode = "triple"
        elif self.level == 5:
            self.fire_mode = "super"
        elif self.level >= 6:
            self.fire_mode = "super_2"
    def get_shoot_cooldown(self):
        return max(self.base_shoot_cooldown, PLAYER_MIN_SHOOT_COOLDOWN)
    def get_point(self, points=1):
        self.points += points
        self.check_extra_level()

    def check_extra_level(self):
        while self.points >= self.next_level_threshold:
            self.level += 1
            self.next_level_threshold *= 5
    def shoot(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(90)
        if self.fire_mode == "single":
            Shot(
                self.position.x + forward.x * self.radius,
                self.position.y + forward.y * self.radius,
                forward
            )
        elif self.fire_mode == "double":
            offsets = [-8, 8]
            for offset in offsets:
                pos = self.position + right * offset
                Shot(pos.x, pos.y, forward)
        elif self.fire_mode == "triple":
            angles = [0, -10, 10]
            for angle in angles:
                dir = forward.rotate(angle)
                pos = self.position + dir * self.radius
                Shot(pos.x, pos.y, dir)
        elif self.fire_mode == "super":
            angles = [5, -10, 10, -5]
            for angle in angles:
                dir = forward.rotate(angle)
                pos = self.position + dir * self.radius
                Shot(pos.x, pos.y, dir)
        elif self.fire_mode == "super_2":
            angles = [0, 5, -10, 10, -5]
            for angle in angles:
                dir = forward.rotate(angle)
                pos = self.position + dir * self.radius
                Shot(pos.x, pos.y, dir)
        elif self.fire_mode == "super_3":
            angles = [0, 5, -10, 10, -5]
            for angle in angles:
                dir = forward.rotate(angle)
                pos = self.position + dir * self.radius
                Shot(pos.x, pos.y, dir*2)
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt  # Cooldown runterzählen

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(+1, dt)
        if keys[pygame.K_w]:
            self.move(+1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)

        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
            self.cooldown = self.get_shoot_cooldown()
        if self.invincible:
            self.invincible_timer -= dt
            if self.invincible_timer <= 0:
                self.invincible = False
    
