# #Hang man -> For % While Loops , If / else , Strings , Range , Modules

# #Step 1 

# word_list = ["aardvark", "baboon", "camel"]

# #TO-DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# #TO-DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# #TO-DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# #TO-DO-4 - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# #TO-DO-5 - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# #TO-DO-6- Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# import random 
# chosen_word = random.choice(word_list) # The randomly chosen word is assigned 
# guess_letter = input("Guess a letter: ").lower() # the letter is input by the user 
# word_len=len(chosen_word)
# display=[]
# for lenth in range(0,word_len): #The range is with (0 to n-1) so if babbon is 6 , in range its 0-5 
#     display.append("_")
# print(display)
# print(f"PS :the solution is {chosen_word} ")

# # For a letter given by thw user  to be checked if that letter is available in the randomly chosen word
# # so in a way For each letter in the chosen_word is checked with the given letter and provided an answer
# # for example if the chosen word is babbon 
# #  for 'a'  in ['b','a','b','b','o','n']
# #  a in [0] = a != b :- Wrong
# #  a in [0] = a == a :- right
# #  a in [0] = a != b :- Wrong
# #  a in [0] = a != b :- Wrong
# #  a in [0] = a != o :- Wrong
# #  a in [0] = a != n :- Wrong

# # Step -1 for loop
# # for letter in chosen_word:
# #     if letter == guess_letter:
# #         display.append(letter)
# #     else:
# #         print("wrong")

# for position in range(word_len):
#     letter = chosen_word[position]
#     if letter == guess_letter:
#         display[position] = letter
        
        
# print(display)

# # #Step -2
# import random
# from turtle import pos
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# word_len = len(chosen_word)
# display=[]
# for _ in range(word_len):
#     display+= "_"
# #TO-DO-1: - Use a while loop to let the user guess again. The loop should only 
# # stop once the user has guessed all the letters in the chosen_word and 'display' 
# # has no more blanks ("_"). Then you can tell the user they've won.
# end_of_game = False
# while not end_of_game:
#     guess_letter=input(" Guess a Letter : ")


#     for position in range(word_len):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current Letter :{letter}\n Guessed Letter :{guess_letter}")
#         if letter == guess_letter:
#             display[position]= letter
#     print(display)
    
#     if "_" not in display:
#         end_of_game = True
#         print("You win")

# Step-3 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6
#TO-DO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Set up for Blanks
display=[]
for _ in range(word_len):
    display+= "_"

end_of_game = False
while not end_of_game:
    guess_letter=input(" Guess a Letter : ")
#TO-DO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.

    for position in range(word_len):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current Letter :{letter}\n Guessed Letter :{guess_letter}")
        if letter == guess_letter:
            display[position]= letter
          
    if guess_letter not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")
#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win")
  #TO-DO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])