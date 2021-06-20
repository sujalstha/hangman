import random
import time

words = ['Opera', 'Zeppelin', 'Jazz', 'Juneteenth', 'Github']
name = input("What is your name? ")
time.sleep(1)
print("\nHello, " + name, "its time to play Hangman!")
time.sleep(1)
print('\nStart Guessing\n--------------')

ele_word = random.choices(words)

guesses = ''

for word in ele_word:
    ele_word = word

turn = 15

while turn > 0:
    won = 1

    for letter in ele_word:
        if letter in guesses:
            print(letter)
        else:
            print('-')
            won -= 1

    guess = input("guess a letter: ")
    guesses += guess

    if guess not in ele_word:
        turn -= 1
        print("\nWrong Try Again\nYou have", turn, "guesses.")

    if turn == 0:
        print("Game Over, sorry you lost :C")

    if won == 0:
        print("You Win, good job! :)")


