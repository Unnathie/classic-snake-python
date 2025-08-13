# 🐍 Nostalgic Snake Game (Python Turtle)

> **Choose Your Mode:**
> ```
> 🎮 Classic Mode      →  python "main .py"         (No high score, pure nostalgia)
> 🏆 High Score Mode   →  python updated_main.py    (Persistent high score & extras)
> ```

A polished revival of the classic Snake game, handcrafted in Python with the `turtle` graphics library.  
Run it as it was… or supercharge it with **persistent high score tracking**. Your call.

---

## ✨ Features

- **Smooth & Snappy** : Crisp turns, responsive controls, no sluggish snakes here.
- **Stylish Snacks** : Magenta, turtle-shaped food. Because why not?
- **Two Ways to Play**:  
  - **`main.py`** : Original game, no high score saved (pure nostalgia).  
  - **`updated_main.py`** : Upgraded version with high score saving + display.
- **Optional Upgrades** : Extra `updated_*` modules enhance gameplay but aren’t required.
- **Honest Game Over** : When you crash, it’s loud and clear.
- **Modular & Maintainable** : Code split into snake, food, and scoreboard modules.

---

## 📂 Project Structure

```
classic-snake-python/
├── README.md            # This file (project overview)
├── food.py              # Handles food spawning
├── high_score.txt       # Stores your high score (only used by updated version)
├── main .py             # Original main game loop (no high score persistence)
├── scoreboard.py        # Displays score (base version)
├── snake.py             # Snake logic (base version)
├── updated_main.py      # Main game with persistent high score
├── updated_snake.py     # Updated snake mechanics (optional)
├── updatedscore.py      # Updated scoreboard with high score persistence (optional)
```

---

## 🕹 How to Play

1. **Clone this repo:**
   ```bash
   git clone https://github.com/Unnathie/classic-snake-python.git
   cd classic-snake-python
   ```

2. **Choose your flavor:**
   - Run the classic:
     ```bash
     python "main .py"
     ```
   - Run the high score edition:
     ```bash
     python updated_main.py
     ```

3. **Controls:**
   - `↑` Up
   - `↓` Down
   - `←` Left
   - `→` Right

4. **Objective:**  
   Eat the food, grow longer, rack up points, and avoid walls or your own tail.

---

## 🏆 High Score Mode (Optional)

- **Available only in `updated_main.py`** with updated modules.
- Reads the highest score from `high_score.txt` on startup.
- Updates the file if you beat your record.
- Works even if you rage-quit — your best run is safe.

---

## 📸 Output

**Classic Mode (No High Score)**  
![Gameplay](https://github.com/user-attachments/assets/09e151e1-2a52-4271-99c3-2e38263ff0b9)  
*Pure old-school fun — score resets each run.*

**High Score Mode (Persistent Score)**  
![High Score Gameplay](![Untitled design](https://github.com/user-attachments/assets/b74e8731-6f7e-4b06-bf93-2da084e3310a))  
*Your best runs live forever in `high_score.txt`.*

## 📸 Screenshots
*When it hit's a wall:*

![Wall Hit](https://github.com/user-attachments/assets/3cbd0adf-80e1-495b-b11e-c4f370a9c7f1)  
*When it hit's itself*

![Tail Hit](https://github.com/user-attachments/assets/74fd6324-a8ee-48a1-9805-577637b9d21a)
---

## 📌 Requirements

- **Python 3.x**
- **turtle** (bundled with Python — no installs needed)

---

## 🚀 Future Upgrades

- **Pause/Resume** — Press `P` to take a snack break.
- **Speed Increase** — Snake gets faster as it grows.
- **Obstacles** — More ways to crash.
- **Custom Skins** — Because snakes deserve style too.
- **Retro Sound FX** — For full arcade immersion.

---

🎯 **Pro Tip:** The updated version saves your glory.  
💾 **Pro Fact:** The original version is crash-friendly nostalgia.

Enjoy — whether you keep it old school or embrace the high score chase.
