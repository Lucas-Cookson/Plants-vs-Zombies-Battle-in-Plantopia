# Plants vs. Zombies Phase 3 - Quick Start Guide

## Installation & Running

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Game
```bash
python main.py
```

Game window will open to Level 1. You're ready to play!

## Game Controls

### Mouse
- **Click on SUNS**: Collect falling suns for resources
- **Click PLANT BUTTONS**: Select a plant type (shows cost in suns)
- **Click GAME BOARD**: Place selected plant in grid

### Keyboard
- **R Key** (when lost): Restart current level
- **G Key** (when lost): Restart from Level 1
- **ESC or Close Window**: Quit game

## Gameplay Basics

### Objective
Defeat all spawning zombies to advance to the next level. Complete all 3 levels to win!

### Resource Management
- Start each level with **50 suns**
- Suns fall randomly from top of screen
- Click to collect suns (+25 per click)
- Each plant costs suns to place:
  - **Walnut**: 50 suns (defensive barrier)
  - **Sunflower**: 100 suns (shoots projectiles)
  - **SlowPea**: 150 suns (slows zombies)

### Plant Strategy
- **Sunflower**: Use for damage output, shoots automatically
- **Walnut**: Place to block zombies, very durable
- **SlowPea**: Place strategically to slow enemy advances
- **Tip**: Mix plant types for best defense

### Levels

#### Level 1 (Easy)
- Only regular zombies
- Slower spawn rate
- Max 10 zombies
- Great tutorial for learning mechanics

#### Level 2 (Medium)
- Regular + Fast zombies
- Mixed difficulty
- Max 15 zombies
- Strategy becomes important

#### Level 3 (Hard) - Boss Level
- Regular + Fast + Armored (boss) zombies
- All three zombie types
- Armored zombies have 200 health (very tough!)
- Max 20 zombies
- Requires careful planning and positioning

### Zombie Types
- **Regular Zombie** (gray): Balanced threat
- **Fast Zombie** (red): Quick but weaker
- **Armored Zombie** (dark): Slow but very strong

## Tips & Tricks

1. **Sunflower Spam**: Early on, place multiple sunflowers for damage
2. **Defensive Line**: Use walnuts to create a barrier
3. **Sun Efficiency**: Collect suns before placing expensive plants
4. **SlowPea Placement**: Put SlowPeas ahead of walnuts for extra time
5. **Lane Strategy**: Focus on lanes with most threats
6. **Grid Placement**: Each grid square can hold only one plant
7. **Health Bars**: Watch plant and zombie health bars
8. **Wave Management**: Let sunflowers weaken zombies before walnuts take hits

## Troubleshooting

**Game won't start**
- Ensure Python 3.8+ is installed
- Check pygame is installed: `pip install pygame`
- Try: `python -m main`

**Suns not falling**
- They spawn randomly, wait a few seconds
- Try clicking faster to collect resources
- Check sun counter in top-left of sidebar

**Plants not placing**
- Make sure you have enough suns
- Check that grid square isn't occupied
- Select a plant first (click button)

**Game freezes**
- This shouldn't happen! Report if it does
- Try closing and restarting

## Screen Layouts

### Main Game Screen
```
[SIDEBAR]           [GAME BOARD]
Suns: XX            Lanes with plants/zombies
Plant Buttons       Grid squares (100x110)
                    
[STATUS BAR: Level 1/3 | Plants: X | Zombies: X]
```

### Level Complete Screen
Shows level completion message and auto-advances in 3 seconds

### Loss Screen
Shows "GAME OVER" with restart options:
- Press **R** to retry level
- Press **G** to start over from Level 1

### Victory Screen
Shows "YOU WIN!" after beating all 3 levels

## Statistics

- **Total Plant Types**: 3
- **Total Zombie Types**: 3
- **Total Levels**: 3
- **Max Zombies Per Level**: 10, 15, 20
- **Grid Size**: 800x550 (excluding UI)
- **Lanes**: 5 horizontal rows
- **FPS**: 60 frames per second

## Enjoy!

The game is designed to be challenging but fair. Good luck defeating all the zombies and clearing all three levels!

For more detailed information, see:
- **PHASE3_README.md** - Complete game documentation
- **PHASE3_IMPLEMENTATION.md** - Technical implementation details
