from termcolor import colored, cprint
from pynput import keyboard
import threading
import random
import os

SNAKE_FRAME = chr(9632) 
APPLE_FRAME = "@"

ROWS, COLS = 10, 20
snake = [(ROWS//2, COLS//2)]  
direction = "RIGHT"
apple = None
running = True

def instructions():
    """Print the game instructions"""
    cprint("Gaming mechanics", "yellow")
    print(f"The snake will be ({SNAKE_FRAME})\nThe apple to eat will be ({APPLE_FRAME})")
    print(f"Use {colored('WASD or ARROWS', 'cyan')} to move")

def create_game(rows=ROWS, cols=COLS):
    """Create the initial board"""
    return [["." for _ in range(cols)] for _ in range(rows)]

def gen_apple(snake, rows=ROWS, cols=COLS):
    """Generate apple in free cell"""
    free = [(r, c) for r in range(rows) for c in range(cols) if (r, c) not in snake]
    return random.choice(free)

def draw_board(snake, apple):
    os.system("cls" if os.name == "nt" else "clear")
    board = create_game()
    for r, c in snake:
        board[r][c] = SNAKE_FRAME
    ar, ac = apple
    board[ar][ac] = APPLE_FRAME
    for row in board:
        print("".join(row), flush = True)

def on_press(key):
    global direction, running
    try:
        if key.char in ['w','a','s','d']:
            if key.char == 'w': direction = "UP"
            if key.char == 's': direction = "DOWN"
            if key.char == 'a': direction = "LEFT"
            if key.char == 'd': direction = "RIGHT"
    except AttributeError:
        if key == keyboard.Key.up: direction = "UP"
        if key == keyboard.Key.down: direction = "DOWN"
        if key == keyboard.Key.left: direction = "LEFT"
        if key == keyboard.Key.right: direction = "RIGHT"
        if key == keyboard.Key.esc: running = False

def move_snake():
    global snake, apple, running
    head_r, head_c = snake[0]
    if direction == "UP": head_r -= 1
    if direction == "DOWN": head_r += 1
    if direction == "LEFT": head_c -= 1
    if direction == "RIGHT": head_c += 1
    new_head = (head_r, head_c)

    if (new_head in snake or head_r < 0 or head_r >= ROWS or head_c < 0 or head_c >= COLS):
        running = False
        return

    snake.insert(0, new_head)
    if new_head == apple:
        apple = gen_apple(snake)
    else:
        snake.pop()

def game_loop():
    global apple, running
    apple = gen_apple(snake)
    while running:
        draw_board(snake, apple)
        move_snake()
        threading.Event().wait(0.12) 

if __name__ == "__main__":
    instructions()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    game_loop()
    print("Game Over!")
