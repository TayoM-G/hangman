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
