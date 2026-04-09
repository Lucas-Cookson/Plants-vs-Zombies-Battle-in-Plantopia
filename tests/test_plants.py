"""Tests for plant behavior."""
import unittest
from model import Plant, PlantType

class TestPlants(unittest.TestCase):
    """Test plant health and behavior."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sunflower = Plant(100, 60, 0, PlantType.SUNFLOWER)
        self.walnut = Plant(200, 60, 0, PlantType.WALNUT)
    
    def test_plant_creation(self):
        """Test plant creation."""
        self.assertEqual(self.sunflower.x, 100)
        self.assertEqual(self.sunflower.y, 60)
        self.assertEqual(self.sunflower.lane, 0)
        self.assertTrue(self.sunflower.is_alive())
    
    def test_plant_type(self):
        """Test plant types."""
        self.assertEqual(self.sunflower.plant_type, PlantType.SUNFLOWER)
        self.assertEqual(self.walnut.plant_type, PlantType.WALNUT)
    
    def test_plant_health(self):
        """Test plant health system."""
        initial_health = self.sunflower.health
        self.sunflower.take_damage(10)
        self.assertEqual(self.sunflower.health, initial_health - 10)
        self.assertTrue(self.sunflower.is_alive())
    
    def test_plant_death(self):
        """Test plant dies when health reaches 0."""
        self.sunflower.take_damage(400)
        self.assertFalse(self.sunflower.is_alive())
    
    def test_plant_partial_damage(self):
        """Test plant takes partial damage but survives."""
        self.sunflower.take_damage(100)
        self.assertEqual(self.sunflower.health, 300)
        self.assertTrue(self.sunflower.is_alive())
    
    def test_plant_shoot_cooldown(self):
        """Test plant shoot cooldown."""
        self.assertEqual(self.sunflower.shoot_cooldown, 0)

if __name__ == '__main__':
    unittest.main()
