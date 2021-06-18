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

while True:
    failed = 0

    for char in word:
        if char in word:
            print(char)
        else:
            print("-")