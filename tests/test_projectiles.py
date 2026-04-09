"""Tests for projectile behavior."""
import unittest
from model import Projectile, GameModel

class TestProjectiles(unittest.TestCase):
    """Test projectile movement and collision."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.projectile = Projectile(100, 60, 0)
    
    def test_projectile_creation(self):
        """Test projectile creation."""
        self.assertEqual(self.projectile.x, 100)
        self.assertEqual(self.projectile.y, 60)
        self.assertEqual(self.projectile.lane, 0)
        self.assertEqual(self.projectile.damage, 20)
    
    def test_projectile_movement(self):
        """Test projectile moves right."""
        initial_x = self.projectile.x
        self.projectile.move()
        self.assertEqual(self.projectile.x, initial_x + self.projectile.speed)
        self.assertEqual(self.projectile.x, 105)
    
    def test_projectile_offscreen(self):
        """Test projectile goes offscreen."""
        self.projectile.x = 750
        self.assertFalse(self.projectile.is_offscreen(800))
        self.projectile.x = 810
        self.assertTrue(self.projectile.is_offscreen(800))
    
    def test_projectile_update(self):
        """Test projectile update moves it."""
        initial_x = self.projectile.x
        self.projectile.update()
        self.assertGreater(self.projectile.x, initial_x)

if __name__ == '__main__':
    unittest.main()
