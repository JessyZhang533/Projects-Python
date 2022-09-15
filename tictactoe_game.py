# Play tic tac toe against computer
# 1.f"blablablabla, {...}, blabla. {...}.":f-string formatting
# 2.Can use several '==' in a row to form a condition
# 3.exit(): exit a program; used as an interpreter
# 4.try/except block: check if a line of code will raise an error; if yes, will not exit the program
# 5.random.choice(...): choose one random item from a list, tuple, etc.

import random


board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
player_letter = None
computer_letter = None


def assign_letter(initial_input):
    global player_letter, computer_letter
    " Assign the correct letters to the player and computer "
    if initial_input == 'y':
        player_letter = 'X'
        computer_letter = 'O'
    elif initial_input == 'n':
        player_letter = 'O'
        computer_letter = 'X'
    else:
        initial_input = input("Do you want to go first? (y-you are 'X'; n-you are 'O')")
        assign_letter(initial_input)


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
    while can_convert(player_input) is False or int(player_input) < 1 or int(player_input) > 9 or board[int(player_input) - 1] != '_':
        player_input = get_input_from_player()
    player_input = int(player_input)
    board[player_input - 1] = player_letter


def get_status(board, letter):
    global computer_letter
    " Check if anyone wins or if it's a tie "
    if (board[0] == board[1] == board[2] == letter) or (board[3] == board[4] == board[5] == letter) or (board[6] == board[7] == board[8] == letter):  # 3 in a row
        if letter == computer_letter:
            display_board()
        print(f"{letter} wins!")
        exit()
    elif (board[0] == board[3] == board[6] == letter) or (board[1] == board[4] == board[7] == letter) or (board[2] == board[5] == board[8] == letter):  # 3 in a column
        if letter == computer_letter:
            display_board()
        print(f"{letter} wins!")
        exit()
    elif (board[0] == board[4] == board[8] == letter) or (board[2] == board[4] == board[6] == letter):  # 3 in a diagonal
        if letter == computer_letter:
            display_board()
        print(f"{letter} wins!")
        exit()
    elif '_' not in board:
        display_board()
        print("It's a tie!")
    else:
        if letter == computer_letter:
            display_board()


def computer_move(board, letter):
    " Get a move of the computer(random) "
    move_index = random.randint(1, 9)
    if board[move_index - 1] != '_':
        computer_move(board, letter=letter)
    else:
        board[move_index - 1] = letter


while True:
    initial_input = input("Do you want to go first? (y-you are 'X'; n-you are 'O')")
    assign_letter(initial_input)
    if player_letter == 'X':
        while True:
            player_input = get_input_from_player()
            player_move(player_input, player_letter)
            get_status(board, player_letter)
            computer_move(board, computer_letter)
            get_status(board, computer_letter)
    else:
        while True:
            computer_move(board, computer_letter)
            get_status(board, computer_letter)
            player_input = get_input_from_player()
            player_move(player_input, player_letter)
            get_status(board, player_letter)
