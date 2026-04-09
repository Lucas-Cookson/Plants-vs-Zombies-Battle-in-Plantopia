import pygame
import random
from model import GameModel, ZombieType
from view import GameView
from controller import GameController

def main():
    """Main game entry point."""
    pygame.init()
    
    # Game settings
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    
    # Initialize game components
    model = GameModel()
    view = GameView(model, SCREEN_WIDTH, SCREEN_HEIGHT)
    controller = GameController(model, view)
    
    # Clock for frame rate control
    clock = pygame.time.Clock()
    
    # Main game loop
    while controller.running:
        # Handle events and controller updates
        controller.handle_events()
        
        # Update game logic
        model.update()
        
        # Draw everything
        view.draw()
        
        # Control frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()

