# Play tic tac toe against computer
# 1.f"blablablabla, {...}, blabla. {...}.":f-string formatting

board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def display_board():
    " Display the game board to the player "
    print(f"{board[0]} {board[1]} {board[2]}\n{board[3]} {board[4]} {board[5]}\n{board[6]} {board[7]} {board[8]}")


def get_input_from_player():
    " Get input from player(human) "
    player_input = input("Where to place your next move? (1-9)")
    return player_input


def player_move(player_input, player_letter):
    " Associate the input from the player to a change on the board "
    player_input = int(player_input)
    if player_input < 1 or player_input > 9:
        player_input = int(get_input_from_player())
        player_move(player_input, player_letter=player_letter)
    else:
        board[player_input - 1] = player_letter


player_input = get_input_from_player()
player_move(player_input, 'X')
display_board()
