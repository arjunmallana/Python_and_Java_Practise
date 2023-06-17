# import random

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6


# print(logo)

# #Testing code
# # print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     from hangman_art import stages
#     print(stages[lives])
import hangman_art
import random

words=["aardvark", "baboon", "camel"]
chosen_word = random.choice(words)
len_word=len(chosen_word)
lives=6

display = []


for _ in range(len_word):
    display += "_"

end_of_game = False    

print(f"Psst the chosen word is {chosen_word}")


while not end_of_game :
    guess_letter = input("Guess letter: ").lower
    
    for position in range(len_word):
        letter = chosen_word[position]
        
        if letter == guess_letter:
            display[position] = letter
            
    if guess_letter not in chosen_word:
        lives-=1
        
        if lives == 0:
            end_of_game=True
            print("You lose")
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game=True
        print("You Won")
    print(hangman_art.stages[lives])    
        
        
        
        