import random

class Hangman:
    '''
    This class is used to run a game of Hangman.

    Attributes:
        word (str): The word to be guessed, picked randomly from the w
        
        word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet
        
        num_lives (int): The number of lives the player has at the start of the game.
        
        word_list (list): A list of words
        
        list_of_guesses (list): A list of the guesses that have already been tried. Set this to an empty list initially
    
    '''
    def __init__(self, word_list, num_lives = 5):
        #attributes
        self.word_list = word_list
        self.num_lives = num_lives

        #initializing other attributes
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        
        This function is used to check if the guess is part of the word. If correct, the guess is returned. If incorrect, reduces the player's life and breaks out.

        Returns:
            guess: the guess used that is correct
            num_lives: the remaining lives of player
        
        '''
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!" + guess + " is in the word.")
            for letter in self.word:
                if guess in self.word:
                    guess_index = self.word.index(guess)
                    self.word_guessed[guess_index] = guess 
            self.num_letters = self.num_letters - 1
            return guess
        else:
            self.num_lives = self.num_lives - 1
            print("Sorry," + guess + " is not in the word. Try again.")
            print("You have " + str(self.num_lives) + " lives left.")
            
    
    def ask_for_input(self):
        '''
        
        This function asks and validates guess from user to ensure the guess is a single letter and is alphabetical. If a guess is already entered before, the function will notify the user. If it is the first time a guess has been entered, it will be appended to the list of guesses. Uses check_guess method to validate input guess.

        Returns:
            list of guesses: the list of guesses input by user
        
        '''
        guess = input("Please enter a single letter for your guess \n")
        while True:
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif  guess in self.list_of_guesses:
                print(self.list_of_guesses)
                print("You already tried that letter!")
                break
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
                break

# function to run the game
def play_game(word_list):
    '''
    This function is used to run the game and check for remaining letters and remaining lives to check if game has ended with the users victory or loss.
    '''
    num_lives = 5
    game = Hangman(word_list = word_list, num_lives = num_lives )
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters >= 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break

#Initializing an instance of the game
word_list = ['Banana','Orange','Strawberry','Apple','Chicken']

# Running the game
play_game(word_list)
