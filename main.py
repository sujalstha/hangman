import random
import time

words = ['Opera', 'Zeppelin', 'Jazz', 'Juneteenth', 'Github']
name = input("What is your name? ")
time.sleep(1)
print("Hello, " + name, "its time to play hangman!")
time.sleep(1)
print('start guessing')

word = random.choices(words)

for i in word:
    word = i

turn = 6

while True:
    incorrect = 0

    for char in word:
        if char in word:
            print(char)
        else:
            print("-")
            incorrect += 1

    if turn == 0:
        print("You Win")
        print("The word is: ", word)
        break

    guess = input("guess a letter: ")
    guess += guess

    if guess not in word:
        turn -= 1
        print("Wrong Try Again\nYou have", incorrect)



