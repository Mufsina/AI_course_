
# ♟️ Chess Game - User vs AI (Minimax)

A simple 2D chess game built with **Pygame**, where the **user plays as White** and the **AI plays as Black** using the **Minimax algorithm** with alpha-beta pruning.

---

## 📌 Features

- Traditional 8x8 Chess Board
- Basic legal moves for each piece
- Player plays as White
- AI (Black) responds using Minimax (depth 2)
- Alpha-beta pruning for performance boost
- Visual piece movement and selection
- Basic piece evaluation for AI decision-making

---

## 📸 Screenshot

> Make sure to include a screenshot of your running game here  
> (e.g., chess board with pieces displayed)

---

## 🚀 Getting Started

### 1. **Install Pygame**
Make sure Python and Pygame are installed.

```bash
pip install pygame
```

### 2. **Clone the Repository / Download Files**

Make sure your folder structure includes:

```
your_project/
├── main.py
├── assets/
│   ├── wp.png  # White pawn
│   ├── wr.png  # White rook
│   ├── ...
│   └── bk.png  # Black king
```

> All images should be 64x64 PNGs named by piece (e.g., `wp.png` = white pawn).

### 3. **Run the Game**

```bash
python main.py
```

---

## 🎮 Controls

- Click on a **white piece** to select.
- Click on a **valid square** to move.
- The AI will automatically make its move after yours.

---

## 🧠 AI Logic

- **Minimax algorithm** with depth 2
- **Alpha-Beta Pruning** for optimization
- **Evaluation function** based on material value:
  - Pawn = 1
  - Knight/Bishop = 3
  - Rook = 5
  - Queen = 9
  - King = 0 (not evaluated directly)

---

## 📦 To-Do / Improvements

- Castling, En Passant, Pawn Promotion
- Check / Checkmate / Stalemate detection
- Game reset / menu system
- Better AI with deeper Minimax or Machine Learning
- Move history, timers, UI improvements

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 👨‍💻 Author

Developed by **Sonia Akther Mufsina**  
Feel free to fork and enhance the game!
