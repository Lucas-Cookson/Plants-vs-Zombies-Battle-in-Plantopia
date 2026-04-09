import random
from enum import Enum

class PlantType(Enum):
    SUNFLOWER = 1  # Shoots projectiles
    WALNUT = 2     # Defensive barrier

class ZombieType(Enum):
    REGULAR = 1    # Normal speed and health
    FAST = 2       # Faster but less health

class Plant:
    """Base plant class."""
    def __init__(self, x, y, lane, plant_type):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 50
        self.height = 50
        self.plant_type = plant_type
        self.max_health = 100 if plant_type == PlantType.WALNUT else 100
        self.health = self.max_health
        self.shoot_cooldown = 0

    def take_damage(self, damage):
        """Reduce plant health."""
        self.health -= damage
        return self.health <= 0

    def is_alive(self):
        """Check if plant is still alive."""
        return self.health > 0

    def update(self):
        """Update plant state."""
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Zombie:
    """Base zombie class."""
    def __init__(self, x, y, lane, zombie_type):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 50
        self.height = 50
        self.zombie_type = zombie_type
        self.speed = 1 if zombie_type == ZombieType.FAST else 0.5  # Halved speed
        self.max_health = 30 if zombie_type == ZombieType.FAST else 50
        self.health = self.max_health
        self.eating = False
        self.eating_target = None
        self.eating_cooldown = 0

    def move(self):
        """Move zombie left."""
        if not self.eating:
            self.x -= self.speed

    def eat_plant(self, plant):
        """Start eating a plant."""
        self.eating = True
        self.eating_target = plant
        self.eating_cooldown = 30  # Frames between bites

    def stop_eating(self):
        """Stop eating the current plant."""
        self.eating = False
        self.eating_target = None
        self.eating_cooldown = 0

    def take_damage(self, damage):
        """Reduce zombie health."""
        self.health -= damage
        return self.health <= 0

    def is_alive(self):
        """Check if zombie is still alive."""
        return self.health > 0

    def update(self):
        """Update zombie state."""
        if self.eating and self.eating_cooldown > 0:
            self.eating_cooldown -= 1
        elif self.eating and self.eating_cooldown == 0:
            # Deal damage to plant
            if self.eating_target and self.eating_target.is_alive():
                self.eating_target.take_damage(10)
                self.eating_cooldown = 30
            else:
                self.stop_eating()

class Projectile:
    """Projectile fired by sunflowers."""
    def __init__(self, x, y, lane):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 10
        self.height = 10
        self.speed = 5
        self.damage = 20

    def move(self):
        """Move projectile right."""
        self.x += self.speed

    def is_offscreen(self, screen_width):
        """Check if projectile has left the screen."""
        return self.x > screen_width

    def update(self):
        """Update projectile state."""
        self.move()

class GameLevel:
    """Represents a game level with difficulty parameters."""
    def __init__(self, level_num, sunflower_reward=50, zombie_spawn_rate=0.02, 
                 zombie_types=[ZombieType.REGULAR, ZombieType.FAST], 
                 max_zombies=12):
        self.level_num = level_num
        self.sunflower_reward = sunflower_reward  # Sun earned per sunflower
        self.zombie_spawn_rate = zombie_spawn_rate
        self.zombie_types = zombie_types
        self.max_zombies = max_zombies
        self.zombies_spawned = 0
        self.is_complete = False

    def get_zombie_type(self):
        """Return a random zombie type for this level."""
        return random.choice(self.zombie_types)

class GameModel:
    """Main game model handling all game logic and state."""
    def __init__(self):
        self.lanes = 5
        self.lane_height = 120
        self.width = 800
        self.height = 600
        
        # Game state
        self.plants = [[] for _ in range(self.lanes)]
        self.zombies = [[] for _ in range(self.lanes)]
        self.projectiles = [[] for _ in range(self.lanes)]
        
        # Level management
        self.current_level = 1
        self.levels = {
            1: GameLevel(1, sunflower_reward=50, zombie_spawn_rate=0.005, 
                        zombie_types=[ZombieType.REGULAR], max_zombies=10),
            2: GameLevel(2, sunflower_reward=50, zombie_spawn_rate=0.01, 
                        zombie_types=[ZombieType.REGULAR, ZombieType.FAST], max_zombies=15)
        }
        self.sun = 100  # Starting sun resources
        self.game_won = False
        self.game_lost = False

    def get_current_level(self):
        """Return the current level object."""
        return self.levels.get(self.current_level)

    def add_plant(self, x, lane, plant_type):
        """Add a plant to the game."""
        if lane < 0 or lane >= self.lanes:
            return False
        
        # Check plant cost
        cost = 100 if plant_type == PlantType.SUNFLOWER else 150
        if self.sun < cost:
            return False
        
        # Prevent overlapping plants in the same cell - check strict grid position
        grid_x = (x // 100) * 100  # Snap to grid
        for plant in self.plants[lane]:
            plant_grid_x = (plant.x // 100) * 100
            if abs(plant_grid_x - grid_x) < 60:  # Strict spacing check
                return False
        
        # Snap to grid for consistency
        snapped_x = grid_x + 25
        plant = Plant(snapped_x, lane * self.lane_height + 35, lane, plant_type)
        self.plants[lane].append(plant)
        self.sun -= cost
        return True

    def add_zombie(self, x, lane, zombie_type=None):
        """Add a zombie to the game."""
        if lane < 0 or lane >= self.lanes:
            return
        
        # Check if there's already a zombie too close in this lane (prevent stacking)
        min_spacing = 80  # Minimum pixel distance between zombies
        for existing_zombie in self.zombies[lane]:
            if abs(existing_zombie.x - x) < min_spacing:
                return  # Too close to existing zombie, don't spawn
        
        level = self.get_current_level()
        if zombie_type is None and level:
            zombie_type = level.get_zombie_type()
        
        zombie = Zombie(x, lane * self.lane_height + 35, lane, zombie_type)
        self.zombies[lane].append(zombie)

    def add_projectile(self, x, y, lane):
        """Add a projectile to the game."""
        if 0 <= lane < self.lanes:
            projectile = Projectile(x, y, lane)
            self.projectiles[lane].append(projectile)

    def collides(self, obj1, obj2):
        """Check if two game objects collide using AABB."""
        return (obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x and
                obj1.y < obj2.y + obj2.height and obj1.y + obj1.height > obj2.y)

    def update(self):
        """Update all game state each frame."""
        if self.game_won or self.game_lost:
            return

        level = self.get_current_level()

        # Spawn new zombies based on level spawn rate
        if level and level.zombies_spawned < level.max_zombies:
            for lane in range(self.lanes):
                if random.random() < level.zombie_spawn_rate:
                    self.add_zombie(self.width, lane)
                    level.zombies_spawned += 1

        # Update all game objects
        for lane in range(self.lanes):
            # Update plants
            for plant in self.plants[lane]:
                plant.update()
                
                # Sunflowers shoot
                if plant.plant_type == PlantType.SUNFLOWER and plant.shoot_cooldown == 0:
                    # Shoot at first zombie in lane
                    if self.zombies[lane]:
                        self.add_projectile(plant.x + plant.width, plant.y, lane)
                        plant.shoot_cooldown = 30  # Frames between shots

            # Update zombies
            for zombie in self.zombies[lane]:
                zombie.update()
                zombie.move()

                # Check if zombie reached plants
                if not zombie.eating:
                    for plant in self.plants[lane]:
                        if self.collides(zombie, plant):
                            zombie.eat_plant(plant)
                            break

                # Check if zombie reached left edge
                if zombie.x < 0:
                    self.game_lost = True

            # Update projectiles
            for projectile in self.projectiles[lane]:
                projectile.update()

        # Handle collisions between projectiles and zombies
        for lane in range(self.lanes):
            for projectile in self.projectiles[lane][:]:
                if projectile.is_offscreen(self.width):
                    self.projectiles[lane].remove(projectile)
                    continue

                for zombie in self.zombies[lane][:]:
                    if self.collides(projectile, zombie):
                        if zombie.take_damage(projectile.damage):
                            self.zombies[lane].remove(zombie)
                        if projectile in self.projectiles[lane]:
                            self.projectiles[lane].remove(projectile)
                        break

        # Remove dead plants
        for lane in range(self.lanes):
            self.plants[lane] = [p for p in self.plants[lane] if p.is_alive()]

        # Remove dead zombies
        for lane in range(self.lanes):
            self.zombies[lane] = [z for z in self.zombies[lane] if z.is_alive()]

        # Check level completion
        level = self.get_current_level()
        if level and level.zombies_spawned >= level.max_zombies:
            # All zombies spawned, check if all are defeated
            total_zombies = sum(len(self.zombies[i]) for i in range(self.lanes))
            if total_zombies == 0:
                if self.current_level == 1:
                    self.current_level = 2
                    self.level_reset()
                elif self.current_level == 2:
                    self.game_won = True

    def level_reset(self):
        """Reset game state for a new level."""
        self.plants = [[] for _ in range(self.lanes)]
        self.zombies = [[] for _ in range(self.lanes)]
        self.projectiles = [[] for _ in range(self.lanes)]
        self.sun = 100

    def is_game_over(self):
        """Check if game is over (won or lost)."""
        return self.game_won or self.game_lost
