import random
import time

words = ['Opera', 'Zeppelin', 'Jazz', 'Juneteenth', 'Github']
chances = 6

name = input("What is your name? ")
time.sleep(1)
print("Hello, " + name, "its time to play hangman!")
time.sleep(1)
print('start guessing')

word = random.choices(words)

for i in word:
    word = i

print(word)