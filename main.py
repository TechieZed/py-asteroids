# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    # Set display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()

    # Initialize delta time and player variables
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Print starting message to console
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    while True:

        # Quit the game when window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen color and draw player each frame   
        screen.fill(color=(0,0,0))
        player.update(dt)
        player.draw(screen)

        # Manage delta time and game clock
        pygame.display.flip()
        time.tick(60)
        dt = time.tick()


if __name__ == "__main__":
    main()
