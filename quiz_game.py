# Create a quiz with 4 questions. The user gets one score for evey correct answer.

questions = ["What is the capital of Germany?", "What is the capital of the UK?", "What is the capital of France?", "What is the capital of Spain?"]

key = ["Berlin", "London", "Paris", "Madrid"]

score = 0

for i in range(len(questions)):
    print(questions[i])
    answer = input("Please answer: ")
    if answer == key[i]:
        score += 1
        print("Well done!")
    else:
        print("Wrong answer. The correct answer is {}.".format(key[i]))

print("Your final score: {}".format(score))
