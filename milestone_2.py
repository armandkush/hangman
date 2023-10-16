import random

word_list = ['Banana','Orange','Strawberry','Apple','Chicken']
print(word_list)

guess = input("Please enter a single letter for your guess \n")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")

word = random.choice(word_list)
print(word)