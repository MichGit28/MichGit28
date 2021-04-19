
# Math game
# The program asks the users 5 question about multiplication of numbers between 2-15
# Print the score and how much time it took to answer all 5 questions

import random

import datetime

def math_game():
    begin_time = datetime.datetime.now()
    correct_counter = 0
    print("Welcome to my Math game! \nyou have 5 attempts, try your best:)!")
    for i in range(5):
        print()
        num1 = random.randint(2, 15)
        num2 = random.randint(2, 15)
        correct_answer = num1 * num2
        print(num1, "*", num2, "=")
        user_answer = int(input())
        if user_answer == correct_answer:
            correct_counter += 1
            print("Good!")
        else:
            print("Wrong!")
    end_time = datetime.datetime.now()
    time = (end_time - begin_time)
    print()
    print(f"You got {correct_counter} correct answers")
    print(f"Your time {time}")
math_game()
