import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    internal_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    ### Game Loop Starts
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        
        
        dt = internal_clock.tick(60) / 1000
    ### Game Loop Ends


if __name__ == "__main__":
    main()