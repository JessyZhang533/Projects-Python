from tkinter import Tk
from tkinter import simpledialog, messagebox


main = Tk()
main.withdraw()

questions = ["What is the capital of Germany?", "What is the capital of the UK?", "What is the capital of France?", "What is the capital of Spain?"]

key = ["Berlin", "London", "Paris", "Madrid"]

score = 0

for i in range(len(questions)):
    answer = simpledialog.askstring(questions[i], "Please answer: ")
    if answer == key[i]:
        score += 1
        messagebox.showinfo("Well done!")
    else:
        messagebox.showinfo("Wrong answer. The correct answer is {}.".format(key[i]))

messagebox.showinfo("Your final score", str(score))  # convert the score (int) to a string
