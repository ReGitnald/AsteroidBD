import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_char = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        main_char.update(dt)
        screen.fill("black")
        main_char.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000

if __name__ == "__main__":
    main()