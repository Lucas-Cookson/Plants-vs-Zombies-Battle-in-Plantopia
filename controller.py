import pygame
from model import PlantType

class GameController:
    """Handles user input and game control."""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_plant = None
        self.running = True
        self.click_cooldown = 0  # Prevent rapid clicks

    def handle_events(self):
        """Process pygame events."""
        # Update click cooldown
        if self.click_cooldown > 0:
            self.click_cooldown -= 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.click_cooldown == 0:
                self._handle_mouse_click(event.pos)
                self.click_cooldown = 10  # 10 frame cooldown between clicks
            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)

    def _handle_mouse_click(self, pos):
        """Handle mouse click events."""
        x, y = pos
        
        # If game is lost, clicking on game area doesn't do anything
        # (player must use keyboard to restart)
        if self.model.game_lost:
            return
        
        # Check if clicking on plant selection buttons
        if self.view.sunflower_button.collidepoint(pos):
            self.selected_plant = PlantType.SUNFLOWER
            return
        elif self.view.walnut_button.collidepoint(pos):
            self.selected_plant = PlantType.WALNUT
            return
        elif self.view.slowpea_button.collidepoint(pos):
            self.selected_plant = PlantType.SLOWPEA
            return
        
        # Check if clicking on suns to collect them
        for sun in self.model.suns[:]:
            sun_x = sun.x + self.view.sidebar_width
            sun_y = sun.y
            dist = ((x - sun_x) ** 2 + (y - sun_y) ** 2) ** 0.5
            if dist < sun.width:
                sun.collect()
                self.model.sun_count += 25  # Collect 25 suns per click
                self.model.suns.remove(sun)
                return
        
        # If no plant selected, do nothing
        if self.selected_plant is None:
            return
        
        # Convert screen coordinates to game coordinates
        game_x = x - self.view.sidebar_width
        game_y = y
        
        # Only place plants in the game area
        if game_x < 0 or game_x >= self.view.game_width or game_y >= self.view.game_area_height:
            return
        
        # Place plant if coordinates are valid
        lane = int(game_y / self.model.lane_height)
        if 0 <= lane < self.model.lanes:
            # Round to grid
            plant_x = (game_x // 100) * 100 + 25
            success = self.model.add_plant(plant_x, lane, self.selected_plant)
            
            # Clear selection on successful placement to prevent multiple placements
            if success:
                self.selected_plant = None

    def _handle_key_press(self, key):
        """Handle keyboard input."""
        if key == pygame.K_r and self.model.game_lost:
            # Restart current level
            self.model.restart_current_level()
        elif key == pygame.K_g and self.model.game_lost:
            # Restart from Level 1
            self.model.restart_from_beginning()

