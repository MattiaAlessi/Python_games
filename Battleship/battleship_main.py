"""
Battleship (CLI)

10x10 grid
"""

from termcolor import cprint, colored

# Symbols:
# X = hit
# O = miss
# . = untouched water
# Letters = ships (A,B,D,S,P)

battleship_dict = {
    "Aircraft Carrier": 5,
    "Battleship": 4,
    "Destroyer": 3,
    "Submarine": 3,
    "Patrol Boat": 2
}

def empty_board(size=10):
    """Create an empty board filled with '.'"""
    return [["." for _ in range(size)] for _ in range(size)]

def print_board(board, reveal=False):
    """Print the board with colors for hits, misses, and optionally ships."""
    for line in board:
        for column in line:
            match column:
                case "X":  # hit
                    cprint("X", "red", end=" ")
                case "O":  # miss
                    cprint("O", "green", end=" ")
                case ".":
                    cprint(".", "cyan", end=" ")
                case _:
                    if reveal:
                        cprint(column, "yellow", end=" ")  # show ships
                    else:
                        cprint(".", "cyan", end=" ")       # hide ships
        print()

def can_place(board, x, y, length, orientation):
    """Check if ship fits and does not overlap."""
    size = len(board)
    if orientation == "H":
        if y + length > size:
            return False
        return all(board[x][y+i] == "." for i in range(length))
    else:  # Vertical
        if x + length > size:
            return False
        return all(board[x+i][y] == "." for i in range(length))

def place_ship(board, name, length):
    """Ask player where to place the ship."""
    placed = False
    while not placed:
        try:
            print(f"\nPlace your {name} (length {length})")
            x = int(input("Row (0 - 9): "))
            y = int(input("Column (0 - 9): "))
            orientation = input("Orientation (Horizontal or Vertical): ").upper()

            if can_place(board, x, y, length, orientation):
                if orientation == "H":
                    for i in range(length):
                        board[x][y+i] = name[0]
                else:
                    for i in range(length):
                        board[x+i][y] = name[0]
                placed = True
            else:
                print("Invalid placement")
        except ValueError:
            print("Enter a valid number")

def setup_player(player_name):
    """Create board and place all ships manually."""
    board = empty_board()
    print(f"\n {colored(player_name, 'magenta')} place your fleet\n")
    for ship, length in battleship_dict.items():
        place_ship(board, ship, length)
        print_board(board, reveal=True)
    return board

def take_shot(board, tracking_board):
    """Player fires at opponent's board."""
    try:
        x = int(input("Target row (0-9): "))
        y = int(input("Target col (0-9): "))
        if board[x][y] != "." and board[x][y] not in ["X", "O"]:
            board[x][y] = "X"
            tracking_board[x][y] = "X"
            cprint("Hit", "green")
        else:
            board[x][y] = "O"
            tracking_board[x][y] = "O"
            cprint("Miss", "red")
    except ValueError:
        cprint("Invalid input", "yellow")

def all_sunk(board):
    """Check if all ships are sunk."""
    for row in board:
        for cell in row:
            if cell not in [".", "X", "O"]:
                return False
    return True

def play_game():
    cprint(r"""
          ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
          ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
          ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
          ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
          ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
          ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
          """, "yellow")

    p1_board = setup_player("Player 1")
    p2_board = setup_player("Player 2")

    p1_tracking = empty_board()
    p2_tracking = empty_board()

    turn = 1
    while True:
        if turn == 1:
            print("\nPlayer 1's turn")
            print_board(p1_tracking)
            take_shot(p2_board, p1_tracking)
            if all_sunk(p2_board):
                cprint("Player 1 wins", "magenta")
                break
            turn = 2
        else:
            print("\nPlayer 2's turn")
            print_board(p2_tracking)
            take_shot(p1_board, p2_tracking)
            if all_sunk(p1_board):
                cprint("Player 2 wins", "magenta")
                break
            turn = 1

if __name__ == "__main__":
    play_game()
