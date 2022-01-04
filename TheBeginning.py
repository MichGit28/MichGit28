
# Math game
# The program asks the users 5 question about multiplication of numbers between 2-15
# Prints the score and shows how much time it took to answer all 5 questions

import random

import datetime

def mathGame():
    beginTime = datetime.datetime.now()
    correctCounter = 0
    print("Welcome to my Math game!")
    print("You have 5 attempts, try you best:)!")
    for i in range(5):
        print()
        firstNumber = random.randint(2, 15)
        secondNumber = random.randint(2, 15)
        correctAnswer = firstNumber * secondNumber
        print(firstNumber, "*", secondNumber, "=", end=" ")
        userAnswer = int(input())
        if userAnswer == correctAnswer:
            correctCounter += 1
            print("Good!")
        else:
            print("Wrong!")
    endTime = datetime.datetime.now()
    totalTime = (endTime - beginTime)
    print(f"\nYou got {correctCounter} correct answers")
    print(f"Your time {totalTime}")
mathGame()
