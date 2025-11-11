import pygame, player, circleshape
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    prints()
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    first_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        log_state()
    
        screen.fill("black")
        updatable.update(dt)
        for draw_object in drawable:
            draw_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        

def prints():
    print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
