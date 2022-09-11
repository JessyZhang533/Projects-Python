# Tkinter: a graphic user interface
# 1.Importing, innitialising and hiding windows
# 2. 'simpledialog.askstring(title, prompt)' replaces '.input()'
# 3. 'messagebox.showinfo()' replaces 'print()'
# 4. 'from ... import *' not supported https://www.flake8rules.com/rules/F403.html
# 5. '.mainloop()' see line31
from tkinter import Tk
from tkinter import simpledialog, messagebox

from random import randint


main = Tk()  # Initialise/Create an instance of window
main.withdraw()  # Hide the window


random_number = randint(0, 10)
print("See answer: {}".format(random_number))

while True:
    x = simpledialog.askstring("Guess", "Enter your guess (a number from 0 to 10):")  # Replace '.input()'
    x = int(x)
    if x == random_number:
        messagebox.showinfo("You guessed correctly.")  # Replace print
        break
    elif x < 0 or x > 10:
        messagebox.showinfo("Number out of range.")  # Replace print
    else:
        messagebox.showinfo("Wrong number. Try again.")  # Replace print

main.mainloop()  # Run the tkinter event loop (listens to events such as keypresses and buttonclicks)
