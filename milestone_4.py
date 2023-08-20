import random


word_list = ['apple', 'pear', 'plum', 'orange', 'banana']
word = random.choice(word_list)
print(word)


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = word
        self.word_guessed = ["_"] * len(word)
        self.num_letters = int()
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for letter in enumerate(word):
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