import random
import time

words = ['Opera', 'Zeppelin', 'Jazz', 'Juneteenth', 'Github']
name = input("What is your name? ")
time.sleep(1)
print("\nHello, " + name, "its time to play Hangman!")
time.sleep(1)
print('Start Guessing\n--------------')

words = random.choices(words)

guess = ''

turn = 6

for word in words:
    words = word

print(words)

while True:
    incorrect = 0

    for letter in words:
        if letter in guess:
            print(letter)
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
        print("Wrong Try Again\nYou have", incorrect, " guesses.")

        if turn == 0:
            print("Game Over, sorry you lost :C")



