import random


list_of_fruits = ['apple', 'pear', 'plum', 'orange', 'banana']
word = random.choice(list_of_fruits)
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


ask_for_input() 