import random

word_list = ['Banana','Orange','Strawberry','Apple','Chicken']
word = random.choice(word_list)

def check_guess(guess):
    
    guess = guess.lower()
    if guess in word:
        print("Good guess!" + guess + " is in the word.")
        return guess
    else:
        print("Sorry," + guess + " is not in the word. Try again.")
    
def ask_for_input():
    guess = input("Please enter a single letter for your guess \n")
    check_guess(guess)
    while True:
        if len(guess) == 1 and guess.isalpha() == True:
            print("Good guess!")
            break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
            break

ask_for_input()


