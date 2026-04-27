# Plants vs. Zombies - Phase 3

A complete, playable Plants vs. Zombies game implementation in Python using Pygame.

## Phase 3 Features

### Game Overview
- **Three Complete Levels**: Progressive difficulty from Level 1 through Level 3
- **Three Plant Types**:
  - **Sunflower** ($100): Shoots projectiles horizontally at zombies
  - **Walnut** ($50): Defensive barrier plant with high health
  - **SlowPea** ($150): Slows nearby zombies for tactical advantage

- **Three Zombie Types**:
  - **Regular Zombie**: Standard zombie with moderate health
  - **Fast Zombie**: Quicker movement but lower health
  - **Armored Zombie**: Boss-type zombie with high health (appears in Level 3)

### Resource Economy
- **Sun Collection System**: Suns fall randomly from the top of the screen and stop at random heights
- **Click to Collect**: Click on suns to collect them (25 suns per click)
- **Plant Costs**: Each plant type has a sun cost that must be paid to place it
  - Walnut: 50 suns (most affordable)
  - Sunflower: 100 suns
  - SlowPea: 150 suns (most powerful)
- **Starting Resources**: Players begin with 50 suns

### Level Progression

#### Level 1
- Spawning: Regular zombies only
- Objectives: Basic tutorial level with slower zombie spawn rate
- Completion: Clear all 10 zombies

#### Level 2
- Spawning: Mix of Regular and Fast zombies
- Objectives: Intermediate challenge with faster pacing
- Completion: Clear all 15 zombies

#### Level 3 - Boss Level
- Spawning: Regular, Fast, and Armored (boss) zombies
- Objectives: Final challenge with powerful enemies
- Special Feature: Includes a "boss-style final wave" with Armored zombies
- Completion: Clear all 20 zombies including bosses
- Victory: Defeating Level 3 wins the entire game

### Core Mechanics
- **Collision Detection**: Plants, zombies, and projectiles all interact via AABB collision detection
- **Plant Shooting**: Sunflowers automatically shoot at the first zombie in their lane
- **Zombie Behavior**: Zombies move left and eat plants when adjacent
- **Slowpea Effect**: SlowPea plants slow nearby zombies (within ~80 pixel radius)
- **Health System**: All entities have health bars displayed above them
- **Player Defeat**: Game ends if any zombie reaches the left edge

### Game Over Screen
When the player loses:
- **R key**: Restart the current level
- **G key**: Restart from Level 1

When the player wins:
- Victory screen displays after completing Level 3
- Game displays final congratulations message

## How to Play

### Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run the game: `python main.py`

### Gameplay
1. **Collect Suns**: Click on falling suns to collect them and increase your resources
2. **Select Plants**: Click on plant buttons in the sidebar (shows cost in suns)
3. **Place Plants**: Click on grid squares in the game area to place selected plants
4. **Defend**: Sunflowers shoot automatically; Walnuts block zombies; SlowPeas slow enemies
5. **Progress**: Clear all zombies in a level to advance to the next

### Controls
- **Mouse**: Click to select plants, place plants, and collect suns
- **R**: Restart current level (when game is lost)
- **G**: Restart from Level 1 (when game is lost)
- **Close Window**: Quit game

## Architecture

### Model-View-Controller Design

#### Model (model.py)
Handles all game logic:
- Game state management (plants, zombies, projectiles, suns)
- Collision detection
- Entity updates and physics
- Level management and progression
- Resource economy (sun management)
- Win/lose conditions

#### View (view.py)
Renders all game elements:
- Game board and grid
- Sprites for plants, zombies, projectiles, and suns
- UI sidebar with plant selection buttons
- Status bar showing current level and counts
- Game over and victory screens
- Visual feedback (health bars, slow effects)

#### Controller (controller.py)
Processes user input:
- Mouse clicks for plant selection and sun collection
- Plant placement logic
- Game restart commands
- Input validation

### Supporting Modules

#### assets_manager.py
Creates placeholder sprites programmatically:
- Simple colored shapes for all game entities
- Easily extendable for custom images
- Uses Pygame's drawing functions

#### sounds.py
Sound management system:
- Placeholder for sound effects
- Volume control
- Music management
- Ready for audio integration

## Game Design Notes

### Difficulty Progression
- Level 1: Single zombie type, manageable spawn rate
- Level 2: Two zombie types, increased spawn rate
- Level 3: All zombie types including powerful Armored zombies, highest spawn rate

### Balancing
- Plant costs are balanced against sun income rate
- Sunflower provides continuous offense (most sun-efficient)
- Walnut provides cheap defense
- SlowPea provides tactical slowdown at high cost
- Armored zombies require multiple hits or strategic plant placement

### Visual Feedback
- All entities display health bars
- Slowed zombies show a blue indicator
- Buttons change color based on affordability
- Clear level progression indicators

## Future Enhancements

Possible additions for further development:
- Custom sprite images instead of placeholders
- Sound effects and background music
- Particle effects and animations
- More plant and zombie types
- Power-ups and special abilities
- Leaderboard/scoring system
- Adjustable difficulty settings
- Pause functionality

## File Structure

```
Plants-vs-Zombies-Battle-in-Plantopia/
├── main.py              # Game entry point
├── model.py             # Game logic and state
├── view.py              # Rendering system
├── controller.py        # Input handling
├── sounds.py            # Sound management
├── assets_manager.py    # Asset creation
├── requirements.txt     # Python dependencies
├── tests/               # Unit tests
└── assets/              # Asset files (expandable)
    ├── images/          # Image directory
    └── sounds/          # Audio directory
```

## Requirements

- Python 3.8+
- Pygame 2.1.0+

## Authors

Built as a learning project to demonstrate:
- MVC architecture
- Collision detection
- Game state management
- Object-oriented design
- Python game development

---

Enjoy the game!
