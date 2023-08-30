# Hangman

============================================================================================

## Table of Contents
----------------------------------------
1. Project description
2. Installation instructions
3. Usage instructions
4. Conclusion
5. License information


### 1. Project description
----------------------------------------
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The aim of the project is to produce an online version of the hangman game that is simple and clear for a single user to play.

While completing this project, I have learnt the logical sequence of creating building blocks of code in order to produce an effective and readable final code. I have learnt more about the use of doc strings and comments to enhance the readability of my code and I am learning more about the benefits of using my GitHub README file to expand on my project and ensure optimal usability for the user.

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
      
- Created new Github repo called __hangman__.
- Cloned new GitHub repo onto local system using [hangman](https://github.com/TayoM-G/hangman.git/) (https://github.com/TayoM-G/hangman.git/)

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
- Updated GitHub repo with code changes by staging, committing and pushing changes to my GitHub repo.
  
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

- Milestone 4 continues from milestone 3.
- Created a class called __Hangman__:
  -  Initialised the class using ____init____ mehod and passed __'word_list'__ and __'num_lives'__ as parameters.
  -  Initialised the following attributes: __'word', 'word_guessed', 'num_letters', 'num_lives', 'word_list', 'list_of_guesses'__.
  -  Placed __check_guess__ function within the class as a method and passed __'guess'__ to the method as a parameter:
      - Created a _for_ loop that loops through each letter of the word.
      - Witihin the _for_ loop, I used an _if_ statement to check if the letter is equal to guess.
      - Used the _enummerate_ method to loop through and index each letter.
      - Reuced the variable __'num_letters'__ by one, outside of the _for_ loop.
      - When letter is __NOT__ in the word, used else block to reduce __'num_lives'__ by 1.
      - Printed a message to inform the user that the letter is not in the word and how many lives they have left.
  -  Placed __ask_for_input__ function within the class as a method:
      - Used _elif_ statement to check if __'guess'__ was already in the __'list_of_guesses'__.
      - Printed a message to inform the user that the guess has already been tried.
      - Used else block to call __check_guess__ method when single letter guess is not in __'ist_of_guesses'__.
      - Used _append_ method to add __'guess'__ to the __"list_of_guesses'__.
- Updated GitHub repo with code changes by staging, committing and pushing changes to my GitHub repo.

```python
import random


word_list = ['apple', 'pear', 'plum', 'orange', 'banana']
word = random.choice(word_list)
print(word)


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = word
        self.word_guessed = ["_"] * len(word)
        self.num_letters = len(set(word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

letter_guess = Hangman(['apple', 'pear', 'plum', 'orange', 'banana']) 
letter_guess.ask_for_input()
```
</details>

<details>
<summary> Milestone 5</summary>

</details>


### 4. Conclusion
---------------------------------------------


### 5. License information
---------------------------------------------
