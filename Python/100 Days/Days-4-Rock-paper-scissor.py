# #random module
# #askpython.com
# # import my_module
# import random
# # 1-10
# random_integer = random.randint(1,10)
# print(random_integer)
# # print(my_module.pi)
# # 0.000 - 0.9999
# random_float = random.random()
# print(random_float)
# # 0.0000-4.9999
# random_float2=(random.random())*5
# print(random_float2)

# Random coin toss
# import random
# random_toss = random.randint(0,1)
# if(random_toss==1):
#     print("Heads")
# else:
#     print("Tails")


# coin toss with user input

# import random

# user_choice=input("Heads or Tails\n")
# random_toss = random.randint(0,1)
# if(random_toss==1):
#     result="Heads"
# else:
#     result="Tails"

# if(user_choice =="Heads" and random_toss == 1):
#     print(f"You win ,it is {result}")
# elif(user_choice =="Tails" and random_toss == 0):
#     print(f"You win ,it is {result}")
# else:
#     print(f"You lose, it was {result}")


# Lists

#States of america
# states_of_america={}


# # Import the random module here
# import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# Since the index number starts at 0 and if the names are 3 , then it is 0 1 2
# so we use -1
# random_number = random.randint(0, len(names)-1)
# print(names[random_number] + " is going to buy the meal today!")



# # Index Errors are the most frequent errors you would get
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# col_loc=int(position[0])#1
# row_loc=int(position[1])#1

# selected_row=(map[row_loc-1])
# selected_row[col_loc-1]= "X"


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇23
# print(f"{row1}\n{row2}\n{row3}")

#Rock Paper scissor
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rpslst=(rock,paper,scissors)
comp_choice =random.randint(0,2)
usr_choice=int(input("What do you choose? Type 0 for Rock , for Paper choose 1 and for Scissors choose 2: "))  # noqa: E501
print(rpslst[usr_choice])
print("Computer Chose\n"+rpslst[comp_choice])

if(usr_choice>=3 or usr_choice<0):
    print("invalid entry")  #Invalid input
elif(usr_choice==comp_choice):
    print("Its a draw")     #Same hand so Draw ex: rock and rock
elif(usr_choice == 0 and comp_choice == 2):
    print("You win") #player has rock and computer has scissor
elif(comp_choice == 0 and usr_choice == 2):
    print("You lose")   #computer has rock and player has scissor
elif(usr_choice>comp_choice):
    print("you win") #player has scissor and computer has paper
elif(comp_choice>usr_choice):
    print("you lose")    #computer has scissor and player has paper