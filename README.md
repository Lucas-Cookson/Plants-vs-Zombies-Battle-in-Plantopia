# Plants vs Zombies - Phase 2

**A Python implementation of Plants vs. Zombies using MVC architecture and Pygame**

## Overview

This is an extended version of the Plants vs. Zombies game from Phase 1, rebuilt with enhanced mechanics including multi-level gameplay, projectile systems, health-based combat, and improved graphics.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone [GITHUB_REPOSITORY_URL]
cd Plants-vs-Zombies-Battle-in-Plantopia
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Game

To start the game:
```bash
python main.py
```

## Running Tests

To run all tests:
```bash
python -m pytest tests/
```

Or run individual test files:
```bash
python -m unittest tests.test_plants
python -m unittest tests.test_zombies
python -m unittest tests.test_projectiles
python -m unittest tests.test_collisions
python -m unittest tests.test_levels
```

## Game Features

### Plant Types

1. **Sunflower** (Cost: 50 Sun)
   - Shoots projectiles at zombies
   - Fires every 30 frames when zombies are in lane
   - Health: 100

2. **Walnut** (Cost: 150 Sun)
   - Defensive barrier plant
   - Blocks zombie advancement by being eaten
   - High health (100) to absorb damage
   - Used to create defensive lines

### Zombie Types

1. **Regular Zombie** (Level 1 & 2)
   - Speed: 1 pixel per frame
   - Health: 50
   - Eats plants when reaching them

2. **Fast Zombie** (Level 2 only)
   - Speed: 2 pixels per frame (2x faster than regular)
   - Health: 30 (less durable than regular)
   - Spawn more frequently in Level 2

### Gameplay Mechanics

- **Shooting**: Sunflowers automatically shoot at zombies in their lane. Projectiles deal 20 damage.
- **Collision Detection**: AABB (Axis-Aligned Bounding Box) collision detection for all game objects
- **Zombie Eating**: When zombies reach plants, they stop advancing and deal 10 damage every 30 frames
- **Plant Health**: Plants take damage from eating zombies. When health reaches 0, plants are removed
- **Projectiles**: Move across the screen and disappear at edges

### Level Progression

**Level 1:**
- Spawn Rate: 1.5% per frame
- Maximum Zombies: 10
- Zombie Types: Regular only
- Difficulty: Introductory

**Level 2:**
- Spawn Rate: 2.5% per frame
- Maximum Zombies: 15
- Zombie Types: Regular and Fast
- Difficulty: Significantly harder
- After defeating all Level 2 zombies, victory screen appears

## Architecture

### Model-View-Controller (MVC) Pattern

**Model (`model.py`):**
- Manages all game state and logic
- Classes: Plant, Zombie, Projectile, GameModel, GameLevel
- Handles collision detection, physics, and game rules
- Manages level progression and win/loss conditions

**View (`view.py`):**
- Handles all graphics rendering using Pygame
- Renders plants, zombies, projectiles
- Displays UI (sidebar, status bar, buttons)
- Shows level completion and end screens

**Controller (`controller.py`):**
- Processes user input (mouse clicks)
- Manages plant selection
- Translates user actions to model updates

### Game Loop

The game runs at 60 FPS with the following cycle:
1. **Input**: Handle mouse clicks for plant placement
2. **Update**: Model updates all objects (movement, collisions, animations)
3. **Render**: View draws current game state
4. **Frame Control**: Maintain 60 FPS frame rate

## File Structure

```
.
├── main.py              # Game entry point
├── model.py             # Game logic and state
├── view.py              # Graphics rendering
├── controller.py        # Input handling
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── tests/
    ├── __init__.py
    ├── test_plants.py           # Plant behavior tests
    ├── test_zombies.py          # Zombie behavior tests
    ├── test_projectiles.py      # Projectile tests
    ├── test_collisions.py       # Collision detection tests
    └── test_levels.py           # Level progression tests
```

## Game Controls

- **Left Mouse Click on Sunflower Button**: Select Sunflower
- **Left Mouse Click on Walnut Button**: Select Walnut
- **Left Mouse Click on Grid**: Place selected plant (if you have enough sun and valid position)
- **Close Window**: Exit game

## Testing

The test suite covers:
- Plant health and behavior
- Zombie movement and health
- Projectile movement and collisions
- Collision detection accuracy
- Level progression logic
- Game state management

All tests are non-graphical and focus on game logic.

## Dependencies

- **pygame** (>=2.1.0): Graphics rendering and game framework

See `requirements.txt` for complete dependency list.

## Team and GitHub

This project uses Git and GitHub for version control and team coordination.

GitHub Repository: [GITHUB_REPOSITORY_URL]

### Development Workflow

- Regular commits made throughout development (not just at the end)
- Feature branches for different components
- Pull requests reviewed before merging to main
- GitHub Issues used to track tasks and bugs

## Lessons Learned

In developing Phase 2, several key architectural and programming lessons emerged:

1. **Separation of Concerns**: The MVC pattern proved essential as complexity grew. Keeping game logic separate from rendering made the code more maintainable and testable.

2. **Class Design for Extensibility**: Using base classes (Plant, Zombie) with type systems made it easy to add new plant and zombie variants without refactoring core logic.

3. **State Management**: Properly tracking game states (spawning, eating, alive/dead) was critical for proper game behavior and prevented many subtle bugs.

4. **Entity Component Pattern Benefits**: While not fully implemented, the structure suggests that more complex game features would benefit from an entity-component architecture.

5. **Testing for Game Logic**: Unit tests for non-graphical logic were invaluable. They caught edge cases in collision detection and level progression early.

6. **Performance Considerations**: Managing projectiles and zombies collections efficiently became important as entity count grew.

## Future Enhancements

Potential improvements for later phases:
- Multiple plant/zombie types with specialized abilities
- Sun dropping from killed zombies and defeated plants
- Wave-based level system
- Enhanced graphics with animations
- Sound effects and music
- Settings and difficulty selection
- Leaderboard/score system

## References

1. PopCap Games. "Plants vs. Zombies." 2009. [Https://www.popcap.com/](https://www.popcap.com/)
2. Python Software Foundation. "Python Documentation." Accessed 2026. [https://www.python.org/doc/](https://www.python.org/doc/)
3. Pygame Community. "Pygame Documentation." Accessed 2026. [https://www.pygame.org/](https://www.pygame.org/)
4. Freeman, Eric; Freeman, Elizabeth. "Head First Design Patterns." O'Reilly Media, 2004.

## License

This project is created for educational purposes.

---

**Last Updated**: April 9, 2026

Class Plant:
    Initialize with x, y, lane
    Set width and height to 50

Class Zombie:
    Initialize with x, y, lane
    Set width, height to 50, speed to 1, active to True
    Method move():
        If active, decrement x by speed

Class GameModel:
    Initialize:
        Set lanes to 5, lane_height to 120
        Create empty lists for plants and zombies per lane
    Method add_plant(x, lane):
        Create Plant at x, lane * lane_height + 35, lane
        Add to plants[lane]
    Method add_zombie(x, lane):
        Create Zombie at x, lane * lane_height + 35, lane
        Add to zombies[lane]
    Method update():
        For each lane:
            For each zombie in lane:
                Call move()
                For each plant in lane:
                    If collides(zombie, plant):
                        Set zombie.active to False
    Method collides(zombie, plant):
        Return True if rectangles overlap (AABB collision)
```

#### View Module (Display & Rendering)

```
Class GameView:
    Initialize with root and model
    Create Tkinter canvas with width 800, height 600
    Draw horizontal lines for lanes
    Method draw():
        Delete plant and zombie items (keep lines)
        For each lane:
            For each plant in lane:
                Draw green rectangle
            For each zombie in lane:
                Draw red rectangle
```

#### Controller Module (Input Handling)

```
Class GameController:
    Initialize with model
    Store reference to model
    Method place_plant(event):
        Calculate lane from event.y // model.lane_height
        If valid lane, add plant to model at event.x - 25, lane
```

#### Main Module (Game Loop & Orchestration)

```
Create Tkinter root window
Create GameModel instance
Create GameView instance with root and model
Create GameController instance with model
Bind canvas left-click to controller.place_plant
Add initial zombies in random lanes to model
Define game_loop():
    Call model.update()
    Call view.draw()
    Schedule next update after 50ms
Call game_loop()
Start Tkinter mainloop()
```

## Lessons Learned

Through this project, I learned the importance of separating concerns in software design using the MVC pattern. Implementing the game logic, display, and input handling in separate modules made the code more modular and easier to maintain. I also gained experience with Tkinter for simple graphics and event handling, as well as basic collision detection algorithms. The project reinforced the value of planning the architecture before coding and iteratively testing each component.

## References

[1] Python Software Foundation. "Tkinter — Python interface to Tcl/Tk." Python Documentation, https://docs.python.org/3/library/tkinter.html. Used for creating the graphical user interface and canvas for drawing shapes.

No external Plants vs. Zombies code was used; the implementation is original based on the game concept.
