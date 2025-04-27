import pygame
from constants import *
from shooting import Shot
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        # we will be using this later
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0


    def draw(self, screen, color = "white", width = 2):
        pygame.draw.polygon(screen, color, self.triangle(), width)

    def rotate(self, dt = 1):
        self.rotation += PLAYER_TURN_SPEED * dt
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shoot_timer -= dt
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    

    def shoot(self):
        if self.shoot_timer <= 0:
            bullet = Shot(self.position.x, self.position.y)
            shot_vec = pygame.Vector2(0,1).rotate(self.rotation)* PLAYER_SHOOT_SPEED
            bullet.velocity = shot_vec
            self.shoot_timer = SHOOT_COOLDOWN
