import pygame
from model import PlantType, ZombieType

class GameView:
    """Handles all game rendering using pygame."""
    
    def __init__(self, model, width=800, height=600):
        self.model = model
        self.width = width
        self.height = height
        
        # Colors
        self.BG_COLOR = (200, 220, 100)
        self.LANE_COLOR = (150, 200, 50)
        self.PLANT_COLOR = (0, 200, 0)
        self.WALNUT_COLOR = (139, 69, 19)
        self.SUNFLOWER_COLOR = (255, 215, 0)
        self.ZOMBIE_COLOR = (100, 100, 100)
        self.FAST_ZOMBIE_COLOR = (200, 100, 100)
        self.PROJECTILE_COLOR = (255, 255, 0)
        self.TEXT_COLOR = (0, 0, 0)
        self.SIDEBAR_COLOR = (100, 100, 100)
        self.BUTTON_COLOR = (200, 200, 0)
        self.BUTTON_HOVER_COLOR = (255, 255, 0)
        
        # Screen setup
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Plants vs Zombies - Phase 2")
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)
        
        # Sidebar dimensions
        self.sidebar_width = 150
        self.game_width = width - self.sidebar_width
        
        # Plant selection buttons
        self.sunflower_button = pygame.Rect(10, 10, 130, 40)
        self.walnut_button = pygame.Rect(10, 60, 130, 40)

    def draw(self):
        """Draw the complete game state."""
        self.screen.fill(self.BG_COLOR)
        
        # Draw lane dividers
        for i in range(1, self.model.lanes):
            y = i * self.model.lane_height
            pygame.draw.line(self.screen, self.LANE_COLOR, (self.sidebar_width, y), 
                           (self.width, y), 2)
        
        # Draw game board grid
        for i in range(0, self.game_width, 100):
            pygame.draw.line(self.screen, self.LANE_COLOR, 
                           (self.sidebar_width + i, 0), 
                           (self.sidebar_width + i, self.height - 50), 1)
        
        # Draw all plants
        for lane in range(self.model.lanes):
            for plant in self.model.plants[lane]:
                self._draw_plant(plant)
        
        # Draw all zombies
        for lane in range(self.model.lanes):
            for zombie in self.model.zombies[lane]:
                self._draw_zombie(zombie)
        
        # Draw all projectiles
        for lane in range(self.model.lanes):
            for projectile in self.model.projectiles[lane]:
                self._draw_projectile(projectile)
        
        # Draw sidebar UI
        self._draw_sidebar()
        
        # Draw game status
        self._draw_status()
        
        # Draw end screen if game is over
        if self.model.game_won:
            self._draw_victory_screen()
        elif self.model.game_lost:
            self._draw_loss_screen()
        
        pygame.display.flip()

    def _draw_plant(self, plant):
        """Draw a single plant."""
        x = plant.x + self.sidebar_width
        y = plant.y
        
        if plant.plant_type == PlantType.SUNFLOWER:
            color = self.SUNFLOWER_COLOR
        else:  # WALNUT
            color = self.WALNUT_COLOR
        
        pygame.draw.rect(self.screen, color, 
                        (x, y, plant.width, plant.height))
        
        # Draw health bar
        health_percent = plant.health / plant.max_health
        health_width = plant.width * health_percent
        pygame.draw.rect(self.screen, (100, 255, 100), 
                        (x, y - 5, health_width, 3))
        pygame.draw.rect(self.screen, (200, 0, 0), 
                        (x, y - 5, plant.width, 3), 1)

    def _draw_zombie(self, zombie):
        """Draw a single zombie."""
        x = zombie.x + self.sidebar_width
        y = zombie.y
        
        if zombie.zombie_type == ZombieType.FAST:
            color = self.FAST_ZOMBIE_COLOR
        else:  # REGULAR
            color = self.ZOMBIE_COLOR
        
        pygame.draw.rect(self.screen, color, 
                        (x, y, zombie.width, zombie.height))
        
        # Draw health bar
        health_percent = zombie.health / zombie.max_health
        health_width = zombie.width * health_percent
        pygame.draw.rect(self.screen, (100, 255, 100), 
                        (x, y - 5, health_width, 3))
        pygame.draw.rect(self.screen, (200, 0, 0), 
                        (x, y - 5, zombie.width, 3), 1)
        
        # Draw status if eating
        if zombie.eating:
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + 10, y - 10), 2)

    def _draw_projectile(self, projectile):
        """Draw a single projectile."""
        x = projectile.x + self.sidebar_width
        y = projectile.y
        pygame.draw.circle(self.screen, self.PROJECTILE_COLOR, 
                          (int(x), int(y)), projectile.width // 2)

    def _draw_sidebar(self):
        """Draw the sidebar with controls."""
        pygame.draw.rect(self.screen, self.SIDEBAR_COLOR, 
                        (0, 0, self.sidebar_width, self.height - 50))
        
        # Draw plant selection buttons
        self._draw_button(self.sunflower_button, "Sunflower\n50", 0)
        self._draw_button(self.walnut_button, "Walnut\n150", 1)

    def _draw_button(self, rect, text, button_type):
        """Draw a UI button."""
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
        
        text_surface = self.font_small.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def _draw_status(self):
        """Draw game status information."""
        # Status bar at bottom
        pygame.draw.rect(self.screen, self.SIDEBAR_COLOR, 
                        (0, self.height - 50, self.width, 50))
        
        # Level info
        level_text = self.font_medium.render(
            f"Level: {self.model.current_level}/2", True, self.TEXT_COLOR)
        self.screen.blit(level_text, (10, self.height - 45))
        
        # Sun counter
        sun_text = self.font_medium.render(
            f"Sun: {self.model.sun}", True, self.TEXT_COLOR)
        self.screen.blit(sun_text, (10, self.height - 20))
        
        # Plant/Zombie counts
        plant_count = sum(len(self.model.plants[i]) for i in range(self.model.lanes))
        zombie_count = sum(len(self.model.zombies[i]) for i in range(self.model.lanes))
        
        stats_text = self.font_small.render(
            f"Plants: {plant_count}  |  Zombies: {zombie_count}", True, self.TEXT_COLOR)
        self.screen.blit(stats_text, (300, self.height - 35))

    def _draw_victory_screen(self):
        """Draw victory screen overlay."""
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        level = self.model.current_level - 1
        title = self.font_large.render(f"Level {level} Complete!", True, (0, 255, 0))
        
        if self.model.current_level == 2:
            message = self.font_medium.render("Get ready for Level 2...", True, (255, 255, 255))
        else:
            message = self.font_large.render("YOU WON!", True, (0, 255, 0))
        
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 200))
        self.screen.blit(message, (self.width // 2 - message.get_width() // 2, 300))

    def _draw_loss_screen(self):
        """Draw loss screen overlay."""
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("GAME OVER", True, (255, 0, 0))
        message = self.font_medium.render("Zombies reached your plants!", True, (255, 100, 100))
        
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 200))
        self.screen.blit(message, (self.width // 2 - message.get_width() // 2, 300))
