import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    roid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (roid_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    afield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_char = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # main_char.containers = (main_char)
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in roid_group:
            if asteroid.collide(main_char):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collide(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000

if __name__ == "__main__":
    main()