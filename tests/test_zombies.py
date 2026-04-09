"""Tests for zombie behavior."""
import unittest
from model import Zombie, ZombieType

class TestZombies(unittest.TestCase):
    """Test zombie movement and health."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.regular_zombie = Zombie(750, 60, 0, ZombieType.REGULAR)
        self.fast_zombie = Zombie(750, 60, 1, ZombieType.FAST)
    
    def test_zombie_creation(self):
        """Test zombie creation."""
        self.assertEqual(self.regular_zombie.x, 750)
        self.assertEqual(self.regular_zombie.y, 60)
        self.assertEqual(self.regular_zombie.health, 50)
        self.assertTrue(self.regular_zombie.is_alive())
    
    def test_zombie_speed_regular(self):
        """Test regular zombie speed."""
        self.assertEqual(self.regular_zombie.speed, 1)
    
    def test_zombie_speed_fast(self):
        """Test fast zombie speed."""
        self.assertEqual(self.fast_zombie.speed, 2)
    
    def test_zombie_movement(self):
        """Test zombie moves left."""
        initial_x = self.regular_zombie.x
        self.regular_zombie.move()
        self.assertEqual(self.regular_zombie.x, initial_x - self.regular_zombie.speed)
    
    def test_zombie_damage(self):
        """Test zombie takes damage."""
        initial_health = self.regular_zombie.health
        self.regular_zombie.take_damage(10)
        self.assertEqual(self.regular_zombie.health, initial_health - 10)
        self.assertTrue(self.regular_zombie.is_alive())
    
    def test_zombie_death(self):
        """Test zombie dies when health reaches 0."""
        self.regular_zombie.take_damage(100)
        self.assertFalse(self.regular_zombie.is_alive())
    
    def test_zombie_eating(self):
        """Test zombie eating state."""
        self.assertFalse(self.regular_zombie.eating)
        from model import Plant, PlantType
        plant = Plant(100, 60, 0, PlantType.WALNUT)
        self.regular_zombie.eat_plant(plant)
        self.assertTrue(self.regular_zombie.eating)
        self.assertEqual(self.regular_zombie.eating_target, plant)
    
    def test_zombie_stop_eating(self):
        """Test zombie stops eating."""
        from model import Plant, PlantType
        plant = Plant(100, 60, 0, PlantType.WALNUT)
        self.regular_zombie.eat_plant(plant)
        self.regular_zombie.stop_eating()
        self.assertFalse(self.regular_zombie.eating)
        self.assertIsNone(self.regular_zombie.eating_target)

if __name__ == '__main__':
    unittest.main()
