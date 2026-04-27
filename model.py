import random
from enum import Enum

class PlantType(Enum):
    SUNFLOWER = 1      # Shoots projectiles
    WALNUT = 2         # Defensive barrier
    SLOWPEA = 3        # Slows zombies

class ZombieType(Enum):
    REGULAR = 1        # Normal speed and health
    FAST = 2           # Faster but less health
    ARMORED = 3        # Very high health boss zombie

class Plant:
    """Base plant class."""
    
    # Plant costs in suns
    COSTS = {
        PlantType.SUNFLOWER: 50,
        PlantType.WALNUT: 150,
        PlantType.SLOWPEA: 100
    }
    
    def __init__(self, x, y, lane, plant_type):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 50
        self.height = 50
        self.plant_type = plant_type
        
        # Determine max health based on plant type
        if plant_type == PlantType.WALNUT:
            self.max_health = 150
        else:
            self.max_health = 100
        
        self.health = self.max_health
        self.shoot_cooldown = 0
        self.slow_radius = 80 if plant_type == PlantType.SLOWPEA else 0

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
        
        # Set stats based on zombie type
        if zombie_type == ZombieType.FAST:
            self.speed = 1.5
            self.max_health = 30
        elif zombie_type == ZombieType.ARMORED:
            self.speed = 0.3
            self.max_health = 200
        else:  # REGULAR
            self.speed = 0.5
            self.max_health = 50
        
        self.health = self.max_health
        self.eating = False
        self.eating_target = None
        self.eating_cooldown = 0
        self.slow_duration = 0  # Frames to remain slowed
        self.is_slowed = False

    def move(self):
        """Move zombie left."""
        if not self.eating:
            # Apply slow effect to movement speed
            current_speed = self.speed * 0.5 if self.is_slowed else self.speed
            self.x -= current_speed

    def apply_slow(self, duration=120):
        """Apply slow effect to this zombie."""
        self.is_slowed = True
        self.slow_duration = max(self.slow_duration, duration)

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
        # Update slow duration
        if self.is_slowed:
            self.slow_duration -= 1
            if self.slow_duration <= 0:
                self.is_slowed = False
        
        # Handle eating
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
    """Projectile fired by plants."""
    def __init__(self, x, y, lane, slow_projectile=False):
        self.x = x
        self.y = y
        self.lane = lane
        self.width = 10
        self.height = 10
        self.speed = 5
        self.damage = 20
        self.slow_projectile = slow_projectile  # True if this is a SlowPea projectile

    def move(self):
        """Move projectile right."""
        self.x += self.speed

    def is_offscreen(self, screen_width):
        """Check if projectile has left the screen."""
        return self.x > screen_width

    def update(self):
        """Update projectile state."""
        self.move()

class Sun:
    """Collectible sun resource."""
    def __init__(self, x, y, target_y=None):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = 2  # Falling speed
        # Target y is where the sun stops (random ground position)
        if target_y is None:
            self.target_y = random.randint(100, 450)  # Random height in game area
        else:
            self.target_y = target_y
        self.collected = False
        self.collection_timer = 0  # For animation after collection
        self.floating = False  # Whether it's at rest on the ground

    def fall(self):
        """Make sun fall down the screen."""
        if self.y < self.target_y:
            self.y += self.speed
        else:
            self.floating = True
            self.y = self.target_y

    def update(self):
        """Update sun state."""
        if not self.floating:
            self.fall()

    def collect(self):
        """Mark sun as collected."""
        self.collected = True
        self.collection_timer = 10  # Quick animation frames

class GameLevel:
    """Represents a game level with difficulty parameters."""
    def __init__(self,
                 level_num,
                 sun_spawn_rate=0.01,
                 zombie_spawn_rate=0.02, 
                 zombie_types=[ZombieType.REGULAR, ZombieType.FAST], 
                 max_zombies=12,
                 is_boss_level=False):
        self.level_num = level_num
        self.sun_spawn_rate = sun_spawn_rate  # Probability of sun spawning each frame
        self.zombie_spawn_rate = zombie_spawn_rate
        self.zombie_types = zombie_types
        self.max_zombies = max_zombies
        self.zombies_spawned = 0
        self.is_complete = False
        self.is_boss_level = is_boss_level
        self.boss_wave_started = False
        self.boss_wave_timer = 0

    def get_zombie_type(self):
        """Return a random zombie type for this level."""
        return random.choice(self.zombie_types)

class GameModel:
    """Main game model handling all game logic and state."""
    def __init__(self):
        self.lanes = 5
        self.lane_height = 110
        self.width = 800
        self.height = 600
        self.game_area_width = 800 - 150  # Account for sidebar
        self.game_area_height = 550  # Account for status bar
        
        # Game state
        self.plants = [[] for _ in range(self.lanes)]
        self.zombies = [[] for _ in range(self.lanes)]
        self.projectiles = [[] for _ in range(self.lanes)]
        self.suns = []  # Global sun list
        
        # Resource economy
        self.sun_count = 50  # Starting suns
        self.sun_spawn_timer = 0
        
        # Level management
        self.current_level = 1
        self.levels = {
            1: GameLevel(1, sun_spawn_rate=0.01, zombie_spawn_rate=0.005, 
                        zombie_types=[ZombieType.REGULAR], max_zombies=10),
            2: GameLevel(2, sun_spawn_rate=0.015, zombie_spawn_rate=0.01, 
                        zombie_types=[ZombieType.REGULAR, ZombieType.FAST], max_zombies=15),
            3: GameLevel(3, sun_spawn_rate=0.02, zombie_spawn_rate=0.015,
                        zombie_types=[ZombieType.REGULAR, ZombieType.FAST, ZombieType.ARMORED], 
                        max_zombies=20, is_boss_level=True)
        }
        
        # Game state flags
        self.game_won = False
        self.game_lost = False
        self.level_complete = False
        self.level_complete_timer = 0
        self.restart_level = False
        self.restart_from_level_1 = False

    def get_current_level(self):
        """Return the current level object."""
        return self.levels.get(self.current_level)

    def add_sun(self):
        """Add a randomly spawned sun to the game."""
        x = random.randint(150, self.width - 50)
        y = 0  # Start at top
        target_y = random.randint(100, 450)
        sun = Sun(x, y, target_y)
        self.suns.append(sun)

    def add_plant(self, x, lane, plant_type):
        """Add a plant to the game if player has enough suns."""
        if lane < 0 or lane >= self.lanes:
            return False
        
        # Check if player has enough suns
        cost = Plant.COSTS.get(plant_type, 0)
        if self.sun_count < cost:
            return False
        
        # Prevent overlapping plants in the same cell
        grid_x = (x // 100) * 100
        for plant in self.plants[lane]:
            plant_grid_x = (plant.x // 100) * 100
            if abs(plant_grid_x - grid_x) < 60:
                return False
        
        # Create plant and deduct suns
        snapped_x = grid_x + 25
        plant = Plant(snapped_x, lane * self.lane_height + 35, lane, plant_type)
        self.plants[lane].append(plant)
        self.sun_count -= cost
        return True

    def add_zombie(self, x, lane, zombie_type=None):
        """Add a zombie to the game."""
        if lane < 0 or lane >= self.lanes:
            return
        
        # Check if there's already a zombie too close in this lane
        min_spacing = 80
        for existing_zombie in self.zombies[lane]:
            if abs(existing_zombie.x - x) < min_spacing:
                return
        
        level = self.get_current_level()
        if zombie_type is None and level:
            zombie_type = level.get_zombie_type()
        
        zombie = Zombie(x, lane * self.lane_height + 35, lane, zombie_type)
        self.zombies[lane].append(zombie)

    def add_projectile(self, x, y, lane, slow_projectile=False):
        """Add a projectile to the game."""
        if 0 <= lane < self.lanes:
            projectile = Projectile(x, y, lane, slow_projectile)
            self.projectiles[lane].append(projectile)

    def collides(self, obj1, obj2):
        """Check if two game objects collide using AABB."""
        return (obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x and
                obj1.y < obj2.y + obj2.height and obj1.y + obj1.height > obj2.y)
    
    def distance(self, x1, y1, x2, y2):
        """Calculate distance between two points."""
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def update(self):
        """Update all game state each frame."""
        if self.game_won or self.game_lost:
            return

        level = self.get_current_level()

        # Spawn suns randomly - rate correlates with sunflower count
        if level:
            # Count sunflowers on field
            sunflower_count = sum(1 for lane in range(self.lanes) 
                                for plant in self.plants[lane] 
                                if plant.plant_type == PlantType.SUNFLOWER)
            # Increase spawn rate by 0.005 per sunflower
            adjusted_spawn_rate = level.sun_spawn_rate + (sunflower_count * 0.005)
            if random.random() < adjusted_spawn_rate:
                self.add_sun()
        
        # Update all suns
        for sun in self.suns[:]:
            sun.update()

        # Spawn new zombies based on level spawn rate
        if level and level.zombies_spawned < level.max_zombies:
            for lane in range(self.lanes):
                if random.random() < level.zombie_spawn_rate:
                    self.add_zombie(self.width - 50, lane)
                    level.zombies_spawned += 1

        # Update all game objects
        for lane in range(self.lanes):
            # Update plants
            for plant in self.plants[lane]:
                plant.update()
                
                # SlowPea shoots projectiles that slow zombies
                if plant.plant_type == PlantType.SLOWPEA and plant.shoot_cooldown == 0:
                    if self.zombies[lane]:
                        self.add_projectile(plant.x + plant.width, plant.y, lane, slow_projectile=True)
                        plant.shoot_cooldown = 30

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

                # Check if zombie reached left edge (game over)
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
            total_zombies = sum(len(self.zombies[i]) for i in range(self.lanes))
            if total_zombies == 0 and not self.level_complete:
                self.level_complete = True
                self.level_complete_timer = 180
        
        # Handle level transition
        if self.level_complete:
            self.level_complete_timer -= 1
            if self.level_complete_timer <= 0:
                if self.current_level == 1:
                    self.current_level = 2
                    self.level_reset()
                    self.level_complete = False
                elif self.current_level == 2:
                    self.current_level = 3
                    self.level_reset()
                    self.level_complete = False
                elif self.current_level == 3:
                    self.game_won = True
                    self.level_complete = False

    def level_reset(self):
        """Reset game state for a new level."""
        self.plants = [[] for _ in range(self.lanes)]
        self.zombies = [[] for _ in range(self.lanes)]
        self.projectiles = [[] for _ in range(self.lanes)]
        self.suns = []
        self.sun_count = 50  # Reset sun count for new level

    def restart_current_level(self):
        """Restart the current level."""
        self.level_reset()
        self.game_lost = False
        self.game_won = False
        self.level_complete = False
        level = self.get_current_level()
        if level:
            level.zombies_spawned = 0

    def restart_from_beginning(self):
        """Restart game from Level 1."""
        self.current_level = 1
        self.level_reset()
        self.game_lost = False
        self.game_won = False
        self.level_complete = False
        for level in self.levels.values():
            level.zombies_spawned = 0

    def is_game_over(self):
        """Check if game is over (won or lost)."""
        return self.game_won or self.game_lost
