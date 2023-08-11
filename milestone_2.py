import random

list_of_fruits = ['apple', 'pear', 'plum', 'orange', 'banana']
print(list_of_fruits)

word = random.choice(list_of_fruits)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
