# Hangman

============================================================================================

## Table of Contents
----------------------------------------
1. Project description
2. Installation instructions
3. Usage instructions
4. Conclusion
5. License information


### 1. Project description: ###
----------------------------------------
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


### 2. Installation instructions
---------------------------------------
      a - Open VSCode
      b - open a new terminal
      c - git clone (https://github.com/TayoM-G/hangman.git)
      d - cd to hangman
      e - go to hangman/milestone_5.py
      

### 3. Usage instructions
--------------------------------------

I completed the project over 5 milestones which display the successive stages of my code development. These are as follows:

<details>
<summary>Milestone 1</summary>
      
- Created new Github repo called hangman (https://github.com/TayoM-G/hangman.git/)

</details>

<details>
<summary> Milestone 2</summary>
      
- Milestone 2 cotninues from milestone 1.
- Defined a list of words.
- Chose a random word from the list by importing the _random module_ and using the _choice_ method.
- Assigned the random word to a variable called __'word'__ and printed the __'word'__ variable.
- Asked the user for input and assigned this to a variable called __'guess'__.
- Checked that the input was a single character using an _if-else_ statement.
- When _if_ condition met, printed a message to inform user that their input was accepted.
- When _if_ condition not met, _else_ block is executed and prints a message to inform user that their input was not accepted.
- Updated GitHub repo with code changes by staging, committing and pushing changes to my GitHub repo.

```python
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
```
</details>

<details>
<summary> Milestone 3</summary>

- Milestone 3 cotinues from milestone 2.
- Iteratively checked if the input was a valid guess:
  
  - Created a _while loop_ and set condition to _True_ to  ensure that the code runs continuously.
  - Used code detailed in milestone 2 in the body of the loop to ask the user for input, assign the user input to __'guess'__ variable and check the input is a single letter.
  - Used a _break_ clause to break out of the loop if __'guess'__ variable passes checks.
  - Used else block to print a message to inform the user if __'guess'__ does not pass checks.
  
- Checked whether the guess was in the word:
  
  - Created an _if_ statemnt to check if the guess is in the word.
  - Used a formatted string to print a messgae to inform the user that the guess is in the word.
  - Created a else block to print a message, using a formattted string, to inform the user when guess is not in the word.
    
- Created __check_guess__ and __ask_for_input__ functions to group relevant code:
  
  - __check_guess__ function has __'guess'__ passed in as a parameter and holds the code to check if the guess is in the word.
  - Used the _lower_ method to convert guess into lower case.
  - __ask_for_input__ function contains the code that iteratively checks if the input is a valid guess.
  - The __check_guess__ function is walled within the __ask_for_input__ function but it is executed outside of the _while_ loop.

```python
import random


word_list = ['apple', 'pear', 'plum', 'orange', 'banana']
word = random.choice(word_list)
print(word)


def check_guess(guess):
    """Checks if the letter guessed is in the random word.

    Args:
        guess (str): a single letter input from user.
    """
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    """Checks if user input is valid."""

    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
           break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
```
</details>

<details>
<summary> Milestone 4</summary>

</details>

<details>
<summary> Milestone 5</summary>

</details>


### 4. Conclusion
---------------------------------------------


### 5. License information
---------------------------------------------
