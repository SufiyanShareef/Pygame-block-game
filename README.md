# 🎮 Tetris Game in Python with Pygame


## 🚀 Introduction

Welcome to this classic Block game Tetris implementation built with Python and Pygame! This project recreates the classic beloved puzzle game with all its addictive mechanics. Whether you're a Python enthusiast, game development learner, or just a Tetris fan, this project has something for you!

<div align="center">
  <video src="https://github.com/user-attachments/assets/57a42781-8fdc-4f4e-a362-e14cb81385f4" width="400" height="250" controls></video>
</div>

  



## 🚀 Features 

- **Authentic Gameplay**: All 7 classic Tetrimino shapes (I, O, T, J, L, S, Z)
- **Smooth Controls**:
  - ← → arrows: Move horizontally
  - ↑ arrow: Rotate piece
  - ↓ arrow: Soft drop
  - Space: Hard drop (instant placement)
- **Scoring System**:
  - Single line: 100 points
  - Double lines: 300 points
  - Triple lines: 500 points
  - Tetris (4 lines): 800 points
- **Progressive Difficulty**: Game speeds up as you level up
- **Next Piece Preview**: See what's coming next
- **Game Statistics**: Track score, level, and lines cleared


## 🛠️ Installation

1. **Prerequisites**:
   - Python 3.6+
   - Pygame library

2. **Setup**:
   ```bash
   # Clone the repository
   git clone https://github.com/SufiyanShareef/Pygame-block-game.git
   cd python-tetris

   # Install Pygame
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python tetris.py
   ```

## 🎯 How to Play

| Key          | Action                |
|--------------|-----------------------|
| ← →         | Move left/right       |
| ↑           | Rotate piece          |
| ↓           | Soft drop (faster)    |
| Space       | Hard drop (instant)   |
| R           | Restart (game over)   |
| ESC/Q       | Quit game             |

**Pro Tip**: Try to create "Tetris" (clearing 4 lines at once) for maximum points!

## 🧠 Behind the Code

### Key Components

1. **Game Board**:
   - 10x20 grid represented as 2D list
   - 0 = empty, 1-7 = different Tetrimino types

2. **Tetrimino Class**:
   - Handles piece shapes, colors, and rotation
   - Uses matrix transformation for rotation logic

3. **Game Engine**:
   - Handles collision detection
   - Manages line clearing and scoring
   - Controls game speed progression

### Cool Code Snippets

**Piece Rotation**:
```python
def rotate(self):
    # Transpose and reverse rows for 90° rotation
    return [list(row)[::-1] for row in zip(*self.shape)]
```

**Line Clearing**:
```python
def clear_lines(self):
    # Remove full lines and add new empty ones at top
    self.grid = [row for row in self.grid if not all(row)]
    while len(self.grid) < GRID_HEIGHT:
        self.grid.insert(0, [0]*GRID_WIDTH)
```

## 📈 Performance

The game runs smoothly at 60 FPS with efficient:
- Rendering using Pygame's optimized surface drawing
- Collision detection with boundary checks
- Game state management

## 🤝 Contributing

Love Tetris? Want to improve this implementation? Contributions are welcome!

**Possible Enhancements**:
- Add hold piece functionality
- Implement ghost piece preview
- Add sound effects and music
- Create a high score system

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🎉 Enjoy the Game!

Challenge yourself and see how high you can score! Can you reach Level 10?

```
  _____ _____ _____ _____ _____ 
 |_   _|_   _|_   _|_   _|_   _|
   | |   | |   | |   | |   | |  
   | |   | |   | |   | |   | |  
   |_|   |_|   |_|   |_|   |_|  
```

Let me know your high score! Share on Twitter with #PythonTetris 🚀

> "Block games are simple to learn, but hard to master - just like good code!" 😉
