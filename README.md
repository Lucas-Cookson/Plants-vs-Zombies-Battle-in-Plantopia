# Plants vs Zombies Phase 1

**Author:** [Your Name]  
**Project Name:** Plants vs Zombies Phase 1  
**Date:** March 26, 2026  
**Class:** [Class Name]

## Outline

1. Title Page - Page 1
2. Outline - Page 1
3. Requirements - Page 2
4. Design - Page 3
5. Lessons Learned - Page 5
6. References - Page 6

## Requirements

This project implements a basic version of Plants vs. Zombies using the Model-View-Controller (MVC) architecture. The game features a single level where players can place plants on the screen by clicking the mouse. Zombies spawn on the right side and move towards the left, simulating movement towards the plants.

Key features:
- Plants are represented as green rectangles and are placed at the mouse click position in specific lanes.
- Zombies are represented as red rectangles that move leftward at a constant speed within their lanes.
- Collision detection: When a zombie collides with a plant in the same lane, the zombie stops moving.
- No shooting, attacking, or sun collection mechanics.
- Graphics rendered using Tkinter with simple shapes.

The game separates concerns into three modules:
- **Model (model.py):** Handles game logic, physics, and state (positions, movement).
- **View (view.py):** Manages the display and rendering of game elements.
- **Controller (controller.py):** Processes user input and coordinates the game loop.

Figure 1: Game screenshot (placeholder - simple canvas with rectangles).

## Design

### Pseudocode

#### Model Module

```
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
        Return True if rectangles overlap (standard AABB collision)
```

#### View Module

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

#### Controller Module

```
Class GameController:
    Initialize:
        Create Tkinter root
        Create GameModel instance
        Create GameView instance with root and model
        Bind canvas left-click to place_plant method
        Add initial zombies in random lanes
        Start game_loop
    Method place_plant(event):
        Calculate lane from event.y // lane_height
        If valid lane, add plant at event.x - 25, lane
    Method game_loop():
        Call model.update()
        Call view.draw()
        Schedule next call after 50ms
    Method run():
        Start Tkinter mainloop
```

#### Main Module

```
Import GameController from controller
If __name__ == "__main__":
    Create GameController instance
    Call run()
```

## Lessons Learned

Through this project, I learned the importance of separating concerns in software design using the MVC pattern. Implementing the game logic, display, and input handling in separate modules made the code more modular and easier to maintain. I also gained experience with Tkinter for simple graphics and event handling, as well as basic collision detection algorithms. The project reinforced the value of planning the architecture before coding and iteratively testing each component.

## References

[1] Python Software Foundation. "Tkinter — Python interface to Tcl/Tk." Python Documentation, https://docs.python.org/3/library/tkinter.html. Used for creating the graphical user interface and canvas for drawing shapes.

No external Plants vs. Zombies code was used; the implementation is original based on the game concept.