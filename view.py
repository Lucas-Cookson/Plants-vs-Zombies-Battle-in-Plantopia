import pygame
from model import PlantType, ZombieType, Plant

class GameView:
    """Handles all game rendering using pygame."""
    
    def __init__(self, model, width=800, height=600):
        self.model = model
        self.width = width
        self.height = height
        self.game_area_height = height - 50
        
        # Colors
        self.BG_COLOR = (200, 220, 100)
        self.LANE_COLOR = (150, 200, 50)
        self.WALNUT_COLOR = (139, 69, 19)
        self.SUNFLOWER_COLOR = (255, 215, 0)
        self.SLOWPEA_COLOR = (0, 255, 0)
        self.ZOMBIE_COLOR = (100, 100, 100)
        self.FAST_ZOMBIE_COLOR = (200, 100, 100)
        self.ARMORED_ZOMBIE_COLOR = (50, 50, 50)
        self.PROJECTILE_COLOR = (255, 255, 0)
        self.SUN_COLOR = (255, 200, 0)
        self.TEXT_COLOR = (0, 0, 0)
        self.SIDEBAR_COLOR = (100, 100, 100)
        self.BUTTON_COLOR = (200, 200, 0)
        self.BUTTON_DISABLED_COLOR = (150, 150, 100)
        
        self.sidebar_width = 150
        self.game_width = width - self.sidebar_width
        
        # Screen setup
        try:
            self.screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Plants vs Zombies - Phase 3")
            self.font_large = pygame.font.Font(None, 36)
            self.font_medium = pygame.font.Font(None, 24)
            self.font_small = pygame.font.Font(None, 18)
        except pygame.error:
            self.screen = None
            self.font_large = None
            self.font_medium = None
            self.font_small = None
        
        # Plant buttons
        self.sunflower_button = pygame.Rect(10, 10, 130, 40)
        self.walnut_button = pygame.Rect(10, 60, 130, 40)
        self.slowpea_button = pygame.Rect(10, 110, 130, 40)

    def draw(self):
        """Draw the complete game state."""
        if self.screen is None:
            return
        
        self.screen.fill(self.BG_COLOR)
        
        # Draw lane dividers
        for i in range(1, self.model.lanes):
            y = i * self.model.lane_height
            pygame.draw.line(self.screen, self.LANE_COLOR, (self.sidebar_width, y), 
                           (self.width, y), 2)
        
        # Draw grid
        for i in range(0, self.game_width, 100):
            pygame.draw.line(self.screen, self.LANE_COLOR, 
                           (self.sidebar_width + i, 0), 
                           (self.sidebar_width + i, self.game_area_height), 1)
        
        # Draw suns
        for sun in self.model.suns:
            self._draw_sun(sun)
        
        # Draw plants
        for lane in range(self.model.lanes):
            for plant in self.model.plants[lane]:
                self._draw_plant(plant)
        
        # Draw zombies
        for lane in range(self.model.lanes):
            for zombie in self.model.zombies[lane]:
                self._draw_zombie(zombie)
        
        # Draw projectiles
        for lane in range(self.model.lanes):
            for projectile in self.model.projectiles[lane]:
                self._draw_projectile(projectile)
        
        # Draw UI
        self._draw_sidebar()
        self._draw_status()
        
        # Draw end screens
        if self.model.game_lost:
            self._draw_loss_screen()
        elif self.model.level_complete:
            self._draw_level_complete_screen()
        elif self.model.game_won:
            self._draw_victory_screen()
        
        pygame.display.flip()

    def _draw_sun(self, sun):
        """Draw a sun."""
        x = sun.x + self.sidebar_width
        y = sun.y
        pygame.draw.circle(self.screen, self.SUN_COLOR, (int(x), int(y)), sun.width // 2)
        pygame.draw.circle(self.screen, (200, 150, 0), (int(x), int(y)), sun.width // 2, 2)

    def _draw_plant(self, plant):
        """Draw a plant."""
        x = plant.x + self.sidebar_width
        y = plant.y
        
        if plant.plant_type == PlantType.SUNFLOWER:
            color = self.SUNFLOWER_COLOR
        elif plant.plant_type == PlantType.WALNUT:
            color = self.WALNUT_COLOR
        else:
            color = self.SLOWPEA_COLOR
        
        pygame.draw.rect(self.screen, color, (x, y, plant.width, plant.height))
        
        # Health bar
        health_percent = plant.health / plant.max_health
        health_width = plant.width * health_percent
        pygame.draw.rect(self.screen, (100, 255, 100), (x, y - 5, health_width, 3))
        pygame.draw.rect(self.screen, (200, 0, 0), (x, y - 5, plant.width, 3), 1)

    def _draw_zombie(self, zombie):
        """Draw a zombie."""
        x = zombie.x + self.sidebar_width
        y = zombie.y
        
        if zombie.zombie_type == ZombieType.FAST:
            color = self.FAST_ZOMBIE_COLOR
        elif zombie.zombie_type == ZombieType.ARMORED:
            color = self.ARMORED_ZOMBIE_COLOR
        else:
            color = self.ZOMBIE_COLOR
        
        pygame.draw.rect(self.screen, color, (x, y, zombie.width, zombie.height))
        
        # Health bar
        health_percent = zombie.health / zombie.max_health
        health_width = zombie.width * health_percent
        pygame.draw.rect(self.screen, (100, 255, 100), (x, y - 5, health_width, 3))
        pygame.draw.rect(self.screen, (200, 0, 0), (x, y - 5, zombie.width, 3), 1)
        
        if zombie.eating:
            pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + 10, y - 10), 2)
        
        if zombie.is_slowed:
            pygame.draw.rect(self.screen, (0, 150, 255), 
                           (x, y + zombie.height + 2, zombie.width, 2), 1)

    def _draw_projectile(self, projectile):
        """Draw a projectile."""
        x = projectile.x + self.sidebar_width
        y = projectile.y
        pygame.draw.circle(self.screen, self.PROJECTILE_COLOR, 
                          (int(x), int(y)), projectile.width // 2)

    def _draw_sidebar(self):
        """Draw sidebar UI."""
        pygame.draw.rect(self.screen, self.SIDEBAR_COLOR, 
                        (0, 0, self.sidebar_width, self.height - 50))
        
        if self.font_medium:
            sun_text = self.font_medium.render(f"Suns: {self.model.sun_count}", True, self.SUN_COLOR)
            self.screen.blit(sun_text, (10, self.height - 200))
        
        self._draw_plant_button(self.sunflower_button, "Sunflower", PlantType.SUNFLOWER)
        self._draw_plant_button(self.walnut_button, "Walnut", PlantType.WALNUT)
        self._draw_plant_button(self.slowpea_button, "SlowPea", PlantType.SLOWPEA)

    def _draw_plant_button(self, rect, text, plant_type):
        """Draw a plant button."""
        if self.font_small is None:
            return
        
        cost = Plant.COSTS[plant_type]
        can_afford = self.model.sun_count >= cost
        color = self.BUTTON_COLOR if can_afford else self.BUTTON_DISABLED_COLOR
        
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)
        
        text_surface = self.font_small.render(text, True, self.TEXT_COLOR)
        cost_surface = self.font_small.render(f"${cost}", True, 
                                             self.TEXT_COLOR if can_afford else (100, 100, 100))
        
        self.screen.blit(text_surface, (rect.left + 5, rect.top + 5))
        self.screen.blit(cost_surface, (rect.left + 5, rect.top + 20))

    def _draw_status(self):
        """Draw status bar."""
        pygame.draw.rect(self.screen, self.SIDEBAR_COLOR, 
                        (0, self.height - 50, self.width, 50))
        
        if self.font_medium:
            level_text = self.font_medium.render(f"Level: {self.model.current_level}/3", True, self.TEXT_COLOR)
            self.screen.blit(level_text, (10, self.height - 45))
        
        if self.font_small:
            plant_count = sum(len(self.model.plants[i]) for i in range(self.model.lanes))
            zombie_count = sum(len(self.model.zombies[i]) for i in range(self.model.lanes))
            stats_text = self.font_small.render(
                f"Plants: {plant_count}  |  Zombies: {zombie_count}", True, self.TEXT_COLOR)
            self.screen.blit(stats_text, (200, self.height - 20))

    def _draw_level_complete_screen(self):
        """Draw level complete screen."""
        if self.font_large is None:
            return
        
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render(f"Level {self.model.current_level} Complete!", True, (0, 255, 0))
        
        if self.model.current_level == 1:
            message = self.font_medium.render("Get ready for Level 2...", True, (255, 255, 255))
        elif self.model.current_level == 2:
            message = self.font_medium.render("Get ready for Level 3 - The Final Boss!", True, (255, 255, 255))
        else:
            message = self.font_medium.render("Victory!", True, (255, 255, 255))
        
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 200))
        self.screen.blit(message, (self.width // 2 - message.get_width() // 2, 300))

    def _draw_victory_screen(self):
        """Draw victory screen."""
        if self.font_large is None:
            return
        
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("YOU WIN!", True, (0, 255, 0))
        message = self.font_medium.render("Congratulations! You defeated all zombies!", True, (255, 255, 0))
        
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 200))
        self.screen.blit(message, (self.width // 2 - message.get_width() // 2, 300))

    def _draw_loss_screen(self):
        """Draw loss screen."""
        if self.font_large is None:
            return
        
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("GAME OVER", True, (255, 0, 0))
        message = self.font_medium.render("Zombies reached your plants!", True, (255, 100, 100))
        restart_level = self.font_medium.render("R: Restart Level", True, (200, 200, 0))
        restart_game = self.font_medium.render("G: Restart from Level 1", True, (200, 200, 0))
        
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 150))
        self.screen.blit(message, (self.width // 2 - message.get_width() // 2, 250))
        self.screen.blit(restart_level, (self.width // 2 - restart_level.get_width() // 2, 350))
        self.screen.blit(restart_game, (self.width // 2 - restart_game.get_width() // 2, 400))
