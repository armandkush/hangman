import random

class Hangman:
    
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
            print("You have " + self.num_lives + " lives left.")

    def ask_for_input(self):
        guess = input("Please enter a single letter for your guess \n")
        while True:
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                if self.num_letters != 0:
                    continue
                else:
                    break



word_list = ['Banana','Orange','Strawberry','Apple','Chicken']





