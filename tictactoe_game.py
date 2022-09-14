# Play tic tac toe against computer
# 1.f"blablablabla, {...}, blabla. {...}.":f-string formatting
# 2.Can use several '==' in a row to form a condition
# 3.exit(): exit a program; used as an interpreter
# 4.try/except block: check if a line of code will raise an error; if yes, will not exit the program

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def display_board():
    " Display the game board to the player "
    print(f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}")


def get_input_from_player():
    " Get input from player(human) "
    player_input = input("Where to place your next move? (1-9)")
    return player_input


def can_convert(string):
    " Check if can convert player_input to an integer "
    try:
        int(string)
        return True
    except ValueError:
        return False


def player_move(player_input, player_letter):
    " Associate the input from the player to a change on the board "
    while can_convert(player_input) is False or int(player_input) < 1 or int(player_input) > 9:
        player_input = get_input_from_player()
    player_input = int(player_input)
    board[player_input - 1] = player_letter


def get_status(board, letter):
    " Check if anyone wins or if it's a tie "
    if (board[0] == board[1] == board[2] == letter) or (board[3] == board[4] == board[5] == letter) or (board[6] == board[7] == board[8] == letter):  # 3 in a row
        print(f"{letter} wins!")
        exit()
    elif (board[0] == board[3] == board[6] == letter) or (board[1] == board[4] == board[7] == letter) or (board[2] == board[5] == board[8] == letter):  # 3 in a column
        print(f"{letter} wins!")
        exit()
    elif (board[0] == board[4] == board[8] == letter) or (board[2] == board[4] == board[6] == letter):  # 3 in a diagonal
        print(f"{letter} wins!")
        exit()
    elif '_' not in board:
        print("It's a tie!")
    else:
        pass


def computer_move(board, letter):
    " Program a move of the computer "



while True:
    player_input = get_input_from_player()
    player_move(player_input, 'X')
    display_board()
    get_status(board, 'X')
