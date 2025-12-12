# Flappy Bird 

This project is a personal of **Flappy Bird** game, a bird game, using **Python** and **Pygame**.  
It includes animated spritesheets, a menu system, collision detection, scoring.

---

## ⚙️ Installation & Execution

Make sure Python 3 is installed

1. **Clone or download** the repository.
2. Install pygame package:
```bash
pip install pygame
```
3. Run the menu:
```bash
python3 menu.py
```

---

## Gameplay
- Control a bird that must fly through gaps between pipes.
- Press **SPACE** to jump.
- Pipes are generated randomly and move from right to left.
- The game ends if the bird touch a pipe or goes out of the screen bounds.

## Bird Animation
- The bird uses a **3×3 spritesheet** for animation.
- Each bird frame are extracted using `subsurface()` function and runs in a loop.

## Pipes
- Pipes have:
  - Random heights
  - A fixed gap
- Score increases when passing a pipe.

## Menu System
The menu contain 2 button:
  - **PLAY**
  - **QUIT**
When a player lost, the menu reappears.

---

## 📁 Project Structure
Below are the main folders for the game and their purpose:

### FlappyBird/asset:
Contains all images for the bird animation, screen background and the pipe sprite.

### FlappyBird/flappyBird:
Contains the code to run the game, bird and pipe creation.

### FlappyBird/menu:
Contains the menu's code, (file called to launch the game).

---

## 🧰 Technologies

### Python
- **Python Version:** 3.10  
Main language used to build the game logic.

### Pygame
- **Pygame Version:** 2.5.2  
Used for:
  - Window creation  
  - Rendering (images, text, sprites)  
  - Keyboard input handling  
  - Image transformations (scale, subsurface, flip)

---

## 👤 Author
- **Annita Rasoanaivo**  
Computer Science Student 