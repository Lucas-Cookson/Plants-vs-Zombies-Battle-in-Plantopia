import pygame
from model import PlantType

class GameController:
    """Handles user input and game control."""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_plant = None
        self.running = True

    def handle_events(self):
        """Process pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos)

    def _handle_mouse_click(self, pos):
        """Handle mouse click events."""
        x, y = pos
        
        # Check if clicking on plant selection buttons
        if self.view.sunflower_button.collidepoint(pos):
            self.selected_plant = PlantType.SUNFLOWER
            return
        elif self.view.walnut_button.collidepoint(pos):
            self.selected_plant = PlantType.WALNUT
            return
        
        # If no plant selected, do nothing
        if self.selected_plant is None:
            return
        
        # Convert screen coordinates to game coordinates
        game_x = x - self.view.sidebar_width
        game_y = y
        
        # Only place plants in the game area
        if game_x < 0 or game_x >= self.view.game_width or game_y >= self.model.height - 50:
            return
        
        # Place plant if coordinates are valid
        lane = int(game_y / self.model.lane_height)
        if 0 <= lane < self.model.lanes:
            # Round to grid
            plant_x = (game_x // 100) * 100 + 25
            self.model.add_plant(plant_x, lane, self.selected_plant)

