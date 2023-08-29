# Hangman

## Table of Contents
1. Project description
2. Installation instructions
3. Usage instructions
4. Conclusion
5. License information

### 1. Project description:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### 2. Installation instructions
      a - Open VSCode
      b - open a new terminal
      c - git clone (https://github.com/TayoM-G/hangman.git)
      d - cd to hangman
      e - go to hangman/milestone_5.py

### 3. Usage instructions

####   Milestone 1:
            Created new Github repo ([hangman](https://github.com/TayoM-G/hangman.git)
            
####   Milestone 2:
            Defined a list of words, chose a randomw word from the list by importing random module and using choice method.              Assigned random word to a variable called 'word' and printed the 'word' variable.
'''python
import random

word_list = ['apple', 'pear', 'plum', 'orange', 'banana']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
'''

####   Milestone 3 

####   Milestone 4

####   Milestone 5


### 4. Conclusion


### 5. License information
