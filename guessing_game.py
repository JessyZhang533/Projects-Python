# A guessing game that checks if the number you guess is the same as the random number given
from random import randint


random_number = randint(0, 10)
print(random_number)

while True:
    x = input("Enter your guess (a number from 0 to 9):")
    x = int(x)  # The x input by user is treated as a string, so we need to convert it to an integer
    if x == random_number:
        print("You guessed correctly.")
        break
    elif x < 0 or x > 9:
        print("Number out of range.")
    else:
        print("Wrong number. Try again.")
