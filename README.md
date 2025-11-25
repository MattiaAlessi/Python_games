# Python games collection

This repository contains classic games implemented in Python for the **command line interface** (CLI):

- **Battleship (CLI)** — a two‑player strategy game where players place ships and take turns firing shots.
- **Memory Game (CLI)** — a single‑player card‑matching game where the goal is to find all pairs.


## Battleship (CLI)

### Features
- 10×10 grid board.
- Manual ship placement of the 5 most iconic ships: Aircraft Carrier, Battleship, Destroyer, Submarine, Patrol Boat.
- Colored output:
  - `X` → hit (red)
  - `O` → miss (green)
  - `.` → untouched water (cyan)
  - Ship letters (A, B, D, S, P) shown in yellow when revealed.
- Turn‑based gameplay for two players.
- Win condition: all ships of one player are sunk.

### How to Play
1. Run the script:
   ```bash
   python Battleship/battleship_main.py
   ```


## Memory Game (CLI)

### Features
- Default 4×4 grid (configurable).
- Randomly shuffled pairs of letters (A, B, C…).
- Hidden board with `?` until flipped.
- Colored output:
  - `?` → hidden card (cyan)
  - Revealed letters → yellow
  - Match → green message
  - Miss → red message
- Loop continues until all pairs are found.

### How to Play
1. Run the script:
   ```bash
   python memory/memory_main.py
   ```


> This collection is just the beginning, new CLI games will be added over time.   
> Stay tuned for updates, and feel free to contribute your own ideas!
