import random
import time

words = ['Opera', 'Zeppelin', 'Jazz', 'Juneteenth', 'Github']
name = input("What is your name? ")
time.sleep(1)
print("\nHello, " + name, "its time to play Hangman!")
time.sleep(1)
print('Start Guessing\n--------------')

ele_word = random.choices(words)

guesses = ''

for word in ele_word:
    ele_word = word

while True:
    turn = 15
    incorrect = 6

    for letter in ele_word:
        if letter in guesses:
            print(letter)
        else:
            print("-")

    guess = input("guess a letter: ")
    guesses += guess

    if guess not in ele_word:
        incorrect -= 1
        print("\nWrong Try Again\nYou have", incorrect, "guesses.")

    if turn == 0:
        print("Game Over, sorry you lost :C")
        break

    if guesses == ele_word:
        print("You Win")
        print("The word is: ", ele_word)
        break



