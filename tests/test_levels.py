"""Tests for level progression."""
import unittest
from model import GameModel, GameLevel, ZombieType

class TestLevelProgression(unittest.TestCase):
    """Test level progression and difficulty."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.model = GameModel()
    
    def test_game_starts_at_level_1(self):
        """Test game starts at level 1."""
        self.assertEqual(self.model.current_level, 1)
    
    def test_level_1_exists(self):
        """Test level 1 configuration exists."""
        level = self.model.get_current_level()
        self.assertIsNotNone(level)
        self.assertEqual(level.level_num, 1)
    
    def test_level_2_exists(self):
        """Test level 2 configuration exists."""
        level = self.model.levels[2]
        self.assertIsNotNone(level)
        self.assertEqual(level.level_num, 2)
    
    def test_level_2_harder_than_level_1(self):
        """Test level 2 has higher difficulty."""
        level1 = self.model.levels[1]
        level2 = self.model.levels[2]
        # Level 2 should spawn more zombies
        self.assertGreater(level2.max_zombies, level1.max_zombies)
        # Level 2 spawn rate should be faster
        self.assertGreater(level2.zombie_spawn_rate, level1.zombie_spawn_rate)
    
    def test_level_1_has_regular_zombies(self):
        """Test level 1 has regular zombies."""
        level = self.model.levels[1]
        self.assertIn(ZombieType.REGULAR, level.zombie_types)
    
    def test_level_2_has_multiple_zombie_types(self):
        """Test level 2 has multiple zombie types."""
        level = self.model.levels[2]
        self.assertGreater(len(level.zombie_types), 1)
        self.assertIn(ZombieType.FAST, level.zombie_types)
    
    def test_initial_sun_amount(self):
        """Test initial sun resources."""
        self.assertEqual(self.model.sun, 100)
    
    def test_level_reset(self):
        """Test level reset clears game state."""
        # Add some objects
        self.model.add_plant(100, 0, 1)
        self.model.add_zombie(750, 0)
        self.model.sun = 0
        
        # Reset level
        self.model.level_reset()
        
        # Check state is cleared
        self.assertEqual(len(self.model.plants[0]), 0)
        self.assertEqual(len(self.model.zombies[0]), 0)
        self.assertEqual(self.model.sun, 100)
    
    def test_game_not_won_initially(self):
        """Test game is not won at start."""
        self.assertFalse(self.model.game_won)
    
    def test_game_not_lost_initially(self):
        """Test game is not lost at start."""
        self.assertFalse(self.model.game_lost)

if __name__ == '__main__':
    unittest.main()
