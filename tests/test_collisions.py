"""Tests for collision detection."""
import unittest
from model import GameModel, Plant, Zombie, Projectile, PlantType, ZombieType

class TestCollisions(unittest.TestCase):
    """Test collision detection."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.model = GameModel()
        self.plant = Plant(100, 60, 0, PlantType.WALNUT)
        self.zombie = Zombie(110, 60, 0, ZombieType.REGULAR)
        self.projectile = Projectile(100, 60, 0)
    
    def test_collision_detection_overlap(self):
        """Test collision detection detects overlap."""
        self.assertTrue(self.model.collides(self.plant, self.zombie))
    
    def test_collision_detection_no_overlap(self):
        """Test collision detection rejects non-overlap."""
        self.zombie.x = 300  # Far away
        self.assertFalse(self.model.collides(self.plant, self.zombie))
    
    def test_collision_detection_edge_case(self):
        """Test collision detection at edges."""
        self.zombie.x = 149  # Just touching
        self.assertTrue(self.model.collides(self.plant, self.zombie))
    
    def test_plant_zombie_collision(self):
        """Test plant-zombie collision leads to eating."""
        self.zombie.x = 110
        self.assertFalse(self.zombie.eating)
        if self.model.collides(self.zombie, self.plant):
            self.zombie.eat_plant(self.plant)
        self.assertTrue(self.zombie.eating)
    
    def test_projectile_zombie_collision(self):
        """Test projectile-zombie collision causes damage."""
        self.projectile.x = 110
        initial_health = self.zombie.health
        if self.model.collides(self.projectile, self.zombie):
            self.zombie.take_damage(self.projectile.damage)
        self.assertLess(self.zombie.health, initial_health)

if __name__ == '__main__':
    unittest.main()
