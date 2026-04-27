"""
Simple asset manager for creating placeholder sprites.
"""
import pygame
import os

class AssetManager:
    """Manages game assets (images and sprites)."""
    
    def __init__(self, asset_dir="assets"):
        """Initialize the asset manager."""
        self.asset_dir = asset_dir
        self.images = {}
        self._create_placeholder_images()
    
    def _create_placeholder_images(self):
        """Create simple placeholder sprites programmatically."""
        
        # Create Sunflower sprite
        sunflower = pygame.Surface((50, 50))
        sunflower.fill((200, 220, 100))  # Transparent background
        pygame.draw.circle(sunflower, (255, 215, 0), (25, 25), 15)  # Yellow circle
        pygame.draw.circle(sunflower, (200, 170, 0), (25, 25), 15, 2)  # Border
        self.images['sunflower'] = sunflower
        
        # Create Walnut sprite
        walnut = pygame.Surface((50, 50))
        walnut.fill((200, 220, 100))
        pygame.draw.ellipse(walnut, (139, 69, 19), (10, 15, 30, 30))  # Brown walnut
        pygame.draw.ellipse(walnut, (100, 40, 0), (10, 15, 30, 30), 2)  # Border
        self.images['walnut'] = walnut
        
        # Create SlowPea sprite
        slowpea = pygame.Surface((50, 50))
        slowpea.fill((200, 220, 100))
        pygame.draw.circle(slowpea, (0, 200, 0), (25, 25), 12)  # Green pea
        pygame.draw.polygon(slowpea, (0, 150, 0), [(20, 10), (30, 10), (35, 20)])  # Leaf
        self.images['slowpea'] = slowpea
        
        # Create Regular Zombie sprite
        zombie = pygame.Surface((50, 50))
        zombie.fill((200, 220, 100))
        pygame.draw.rect(zombie, (100, 100, 100), (5, 5, 40, 40))  # Gray body
        pygame.draw.circle(zombie, (0, 0, 0), (15, 15), 3)  # Left eye
        pygame.draw.circle(zombie, (0, 0, 0), (35, 15), 3)  # Right eye
        pygame.draw.line(zombie, (200, 0, 0), (20, 35), (30, 35), 2)  # Red mouth
        self.images['zombie'] = zombie
        
        # Create Fast Zombie sprite
        fast_zombie = pygame.Surface((50, 50))
        fast_zombie.fill((200, 220, 100))
        pygame.draw.rect(fast_zombie, (200, 100, 100), (5, 5, 40, 40))  # Red-tinted body
        pygame.draw.circle(fast_zombie, (0, 0, 0), (15, 15), 3)  # Left eye
        pygame.draw.circle(fast_zombie, (0, 0, 0), (35, 15), 3)  # Right eye
        pygame.draw.polygon(fast_zombie, (255, 0, 0), [(20, 30), (30, 30), (25, 40)])  # Speed triangle
        self.images['fast_zombie'] = fast_zombie
        
        # Create Armored Zombie sprite
        armored_zombie = pygame.Surface((50, 50))
        armored_zombie.fill((200, 220, 100))
        pygame.draw.rect(armored_zombie, (50, 50, 50), (3, 3, 44, 44))  # Dark armor body
        pygame.draw.rect(armored_zombie, (100, 100, 100), (8, 8, 34, 34))  # Inner armor
        pygame.draw.circle(armored_zombie, (255, 255, 255), (15, 15), 2)  # Eye
        pygame.draw.circle(armored_zombie, (255, 255, 255), (35, 15), 2)  # Eye
        self.images['armored_zombie'] = armored_zombie
        
        # Create Projectile sprite
        projectile = pygame.Surface((10, 10))
        projectile.fill((200, 220, 100))
        pygame.draw.circle(projectile, (255, 255, 0), (5, 5), 4)  # Yellow projectile
        self.images['projectile'] = projectile
        
        # Create Sun sprite
        sun = pygame.Surface((30, 30))
        sun.fill((200, 220, 100))
        pygame.draw.circle(sun, (255, 200, 0), (15, 15), 12)  # Yellow sun
        pygame.draw.circle(sun, (200, 150, 0), (15, 15), 12, 2)  # Border
        # Draw rays
        for i in range(8):
            import math
            angle = i * math.pi / 4
            x1 = 15 + 12 * math.cos(angle)
            y1 = 15 + 12 * math.sin(angle)
            x2 = 15 + 18 * math.cos(angle)
            y2 = 15 + 18 * math.sin(angle)
            pygame.draw.line(sun, (255, 200, 0), (x1, y1), (x2, y2), 2)
        self.images['sun'] = sun
        
        # Create background tile
        background = pygame.Surface((100, 110))
        background.fill((150, 200, 50))
        pygame.draw.rect(background, (100, 150, 0), (0, 0, 100, 110), 1)
        self.images['background_tile'] = background
    
    def get_image(self, name):
        """Get a sprite image by name."""
        return self.images.get(name)
    
    def get_all_images(self):
        """Get all available images."""
        return self.images
