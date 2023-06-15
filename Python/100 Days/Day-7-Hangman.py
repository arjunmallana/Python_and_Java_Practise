#Hang man -> For % While Loops , If / else , Strings , Range , Modules
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TO-DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TO-DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TO-DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random 
chosen_word = random.choice(word_list)
guess_letter = input("Guess a letter: ").lower()


for letter in chosen_word:
    if letter == guess_letter:
        print("correct")
    else:
        print("incorrect")