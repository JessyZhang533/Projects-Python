# Play tic tac toe against computer
# 1.f"blablablabla, {...}, blabla. {...}.":f-string formatting

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def display_board():
    " Display the game board to the player "
    print(f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}")


display_board()
