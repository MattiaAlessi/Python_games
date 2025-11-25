"""
Memory Game (CLI)

4x4 grid
"""

import random
from termcolor import cprint, colored

# Symbols:
# ? = hidden card
# Letters = revealed card (A, B, C...)

def create_board(size=4):
    """Create a shuffled board with pairs of letters."""
    # Generate pairs (A, B, C...) depending on grid size
    num_pairs = (size * size) // 2
    letters = [chr(65+i) for i in range(num_pairs)] * 2 
    random.shuffle(letters)
    board = []
    for i in range(size):
        row = letters[i*size:(i+1)*size]
        board.append(row)
    return board

def hidden_board(size=4):
    """Create a hidden board with '?' everywhere."""
    return [["?" for _ in range(size)] for _ in range(size)]

def print_board(board):
    """Print the board with colors for hidden and revealed cards."""
    for line in board:
        for column in line:
            if column == "?":
                cprint("?", "cyan", end=" ")
            else:
                cprint(column, "yellow", end=" ")
        print()

def play_turn(board, visible):
    """Player flips two cards and checks for match."""
    try:
        x1 = int(input("Row of first card (0-3): "))
        y1 = int(input("Col of first card (0-3): "))
        visible[x1][y1] = board[x1][y1]
        print_board(visible)

        x2 = int(input("Row of second card (0-3): "))
        y2 = int(input("Col of second card (0-3): "))
        visible[x2][y2] = board[x2][y2]
        print_board(visible)

        if board[x1][y1] == board[x2][y2]:
            cprint("Match", "green")
        else:
            cprint("Not a match", "red")
            visible[x1][y1] = "?"
            visible[x2][y2] = "?"
    except ValueError:
        cprint("Invalid input", "yellow")

def all_found(visible):
    """Check if all pairs are found."""
    for row in visible:
        for cell in row:
            if cell == "?":
                return False
    return True

def play_game():
    cprint(r"""
     ███╗   ███╗███████╗███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗
     ████╗ ████║██╔════╝████╗ ████║██╔═══██╗██╔══██╗╚██╗ ██╔╝
     ██╔████╔██║█████╗  ██╔████╔██║██║   ██║██████╔╝ ╚████╔╝ 
     ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██╔═══╝   ╚██╔╝  
     ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║        ██║   
     ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝        ╚═╝   
    """, "magenta")

    size = 4
    board = create_board(size)
    visible = hidden_board(size)

    while not all_found(visible):
        print_board(visible)
        play_turn(board, visible)

    cprint("You won", "green")

if __name__ == "__main__":
    play_game()
