import random

list_of_fruits = ['apple', 'pear', 'plum', 'orange', 'banana']
print(list_of_fruits)

fruit = random.choice(list_of_fruits)
print(fruit)

guess = input("Enter a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# it works
