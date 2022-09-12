# 1..geometry(...x... + ... + ...): used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop
# https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
# 2..title():  refers to a name assigned to the application window. It is mostly found on the top of the application
# 3.PIL: Python imaging library; The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.
# 4.label: a Tkinter Widget class used to display text or an image. The label is a widget that the user just views but not interact with.
# https://www.tutorialspoint.com/python/tk_label.htm
# 5..PIL.Image.open(): Opens and identifies the given image file.
import random
from tkinter import Tk, Label
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

main = Tk()
main.geometry("800x600")
main.title("Hangman")
# If we write 'main.withdraw()' here, the window for images would not display

# Load images
image_list = []
for i in range(1, 8):
    image_list.append(Image.open("D:/Studies/2022summer/Udemy/Projects-Python/images/hangman0" + str(i) + ".png"))  # IMPORTANT

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
        user_input = simpledialog.askstring("Hangman", " Please guess one letter: ")
        if user_input not in 'abcdefghijklmnopqrstuvwxyz':
            messagebox.showinfo("Hangman", " Please enter ONE LETTER. ")
        else:
            num_of_guesses += 1
            load_image = ImageTk.PhotoImage(image_list[num_of_guesses - 1])
            label = Label(image=load_image)
            label.image = load_image
            label.place(x=0, y=0)
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
        # messagebox.showinfo("Hangman", user_input) --> ERROR OCCURS, because user_inout already have a title 'Hangman', but here another same title is assigned
        status_now = process_input_and_display(user_input, number)
        messagebox.showinfo("Hangman", status_now)
        if status_now == "You lose!" or status_now == "You win!":
            game_is_done = True
            break

    if game_is_done is True:
        user_choice = simpledialog.askstring("Hangman", "Do you want to play it again? (enter yes or no)")
        if user_choice.lower() == 'yes':  # need to initialise again as follows
            # Generate the word one needs to guess
            correct_word = word_list[random.randint(0, len(word_list) - 1)]
            # messagebox.showinfo("Hangman", "Correct word: {}".format(correct_word))

            # Define global variables
            num_of_guesses = 0
            display_result = "_" * len(correct_word)
            num_of_remaining_letters = len(correct_word)

            # Check if the game is done
            game_is_done = False
        else:
            break
