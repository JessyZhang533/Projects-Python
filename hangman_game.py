# Try to huess a work letter by letter within 10 attempts.
# 1..lower(): make all characters in the given string in lower case; .upper() vice versa
# 2.'end=' parameter and 'sep=' parameter in print()
# 3..split(): split a string into a list where each word is an item; default separator: white space
# 4.Letters in a string can be iterated, can use len() to decide the length, can be indexed into.
# 5.Difference between i+1 and i+=1: https://stackoverflow.com/questions/41446833/what-is-the-difference-between-i-i-1-and-i-1-in-a-for-loop
# 6."UnboundLocalError: local variable '...' referenced before assignment":
# https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
# Cannot set the value of a global variable directly inside a function. Need to declare 'global ...' insidethe top of the function
# 7.'break' statement in a loop within a loop: will only break the inner loop

import random


# Generate the word one needs to guess
word_list = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle fox frog goat goose hawk lion lizard mole monkey moose mouse mule otter owl'.split()
correct_word = word_list[random.randint(0, len(word_list) - 1)]
print("Correct word: {}".format(correct_word))

# Define global variables
num_of_guesses = 0
display_result = "_" * len(correct_word)
num_of_remaining_letters = len(correct_word)

# Check if the game is done
game_is_done = False


def get_input():
    global num_of_guesses
    " Get the input from user and check if it is ONE LETTER; return the letter and increase number of guesses by 1 "
    while True:
        user_input = input(" Please guess one letter: ")
        if user_input not in 'abcdefghijklmnopqrstuvwxyz':
            print(" Please enter one LETTER. ")
        elif len(user_input) != 1:
            print(" Please enter ONE letter. ")
        else:
            num_of_guesses += 1
            return user_input, num_of_guesses


def process_input_and_display(user_input, num_of_guesses):
    global num_of_remaining_letters, display_result
    " Compare the input against letters in the 'correct word', and display the result to user "
    if user_input in correct_word:
        for i in range(len(correct_word)):
            if user_input == correct_word[i]:
                display_result = display_result[:i] + user_input + display_result[(i+1):]
                num_of_remaining_letters -= 1
                if num_of_remaining_letters == 0:
                    return "You win!"
    if num_of_guesses == 7:
        return "You lose!"
    return "Status: {}".format(display_result)


while True:
    # Main body of the game
    while num_of_guesses < 7:
        user_input, number = get_input()
        print(user_input)
        status_now = process_input_and_display(user_input, number)
        print(status_now)
        if status_now == "You lose!" or status_now == "You win!":
            game_is_done = True
            break

    if game_is_done is True:
        user_choice = input("Do you want to play it again? (enter yes or no)")
        if user_choice.lower() == 'yes':  # need to initialise again as follows
            # Generate the word one needs to guess
            correct_word = word_list[random.randint(0, len(word_list) - 1)]
            print("Correct word: {}".format(correct_word))

            # Define global variables
            num_of_guesses = 0
            display_result = "_" * len(correct_word)
            num_of_remaining_letters = len(correct_word)

            # Check if the game is done
            game_is_done = False
        else:
            break
