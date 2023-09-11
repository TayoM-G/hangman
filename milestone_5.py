import random # imports random module


word_list = ['apple', 'pear', 'plum', 'orange', 'banana']


class Hangman:
    """
    A class used to execute Hangman game.

    Parameters:
    ----------
    num_lives: int 
               The number of lives the player has at the start of the game.
    word_list: list
               A list of words.

    Attributes:
    ----------
    word: str
          the word to be guessed, picked at random from word_list.
    word_guessed: list
                  A list of the letters of the word, with _ for each letter not yet guessed.
    num_letters:  int
                  The number of unique letters in the word that have not been guessed yet.
    num_lives: int
               The number of lives the player has at the start of the game.
    word_list: list
               A list of words.
    list_of_guesses: list
                     A list of the guesses that have already been tried.

    """

    def __init__(self, word_list, num_lives = 5):
        """
        Initialises attributes for the Hangman class.
        See class docstring for details of attributes.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def _check_guess(self, guess):
        """
        This method checks that the letter guessed is in the word and replaces 
        corresponding '_' with the letter.

        Parameters:
        ----------
        guess: str
               single letter entered by player.
        """
        guess = guess.lower() 
        # converts the guess to lower case
        if guess in self.word: 
            # checks if guess is in the random word chosen by the computer
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word): 
                # loops through and indexes each letter of the word
                if letter == guess: 
                    # checks if letter is equal to guess
                    self.word_guessed[index] = letter 
                    # places the letter guessed in the corresponding index of the word 
                    # to replace '_'
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")


    def ask_for_input(self):
        """
        This method asks the player to input a single letter, then checks that the 
        input is valid and has not been previouly entered. 
        """
        while True: 
            # iterates over proceeding code 
            guess = input("Enter a single letter: ") 
            # asks user for input and assigns the input to a variable called 'guess'
            if len(guess) != 1 or guess.isalpha() == False: 
                # checks if the input is equal to 1 and is alphabetical
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                # checks if input has already been entered
                print("You already tried that letter!")
            else:
                self._check_guess(guess) 
                # calls check_guess method
                self.list_of_guesses.append(guess) 
                # appends guess to list_of_guesses
                break 


def play_game(word_list):
    """
    This function executes the Hangman game and confirms whether the player has
    won or lost the game.

    Parameters:
    ----------
    word_list: list 
               A list of words.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives) 
    # an instance of the Hangman class. Has word_list and num_lives passed as arguments
    while True: 
        # iterates over proceeding code 
        if game.num_lives == 0: 
            # checks if number of lives is 0
            print("You lost!")
            break
        elif game.num_letters > 0: 
            # checks if number of letters is greater than 0
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0: 
            # checks if number of lives is not 0 and number of letters is not greater 
            # than 0
            print("Congratulations. You won the game!")
            break


play_game(['apple', 'pear', 'plum', 'orange', 'banana'])
