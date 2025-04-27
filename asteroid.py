import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # we will be using this later
        super().__init__(x, y, radius)
        self.rotation = 0


    def draw(self, screen, color = "white", width = 2):
        pygame.draw.circle(screen, color, self.position, self.radius, width)

        

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20, 50)
            plus_angle = self.velocity.rotate(angle)
            minus_angle = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position.x, self.position.y, new_radius)
            ass2 = Asteroid(self.position.x, self.position.y, new_radius)
            ass1.velocity = plus_angle * 1.2
            ass2.velocity = minus_angle * 1.2
        self.kill()

    
    
    # def move(self, dt):
    #     forward = pygame.Vector2(0, 1).rotate(self.rotation)
    #     self.position += forward * PLAYER_SPEED * dt    