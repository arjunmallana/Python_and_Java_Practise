# print("Welcome to the RollerCoster")
# height = int(input("Enter your height in cms :"))
# bill = 0
# if height >= 120:
#     age = int(input("Enter your age: "))
#     if age <= 12:
#         bill += 5
#         print(f"age {age} bill is {bill}")
#     elif age <= 18:
#         bill += 7
#         print(f"age {age} bill is {bill}")
#     elif age > 18 and age < 45:
#         bill += 12
#         print(f"age {age} bill is {bill}")
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("Its on us ")
#     else:
#         bill += 12
#         print("dont care")
# else:
#     print("We are not sure")

# wants_photo = input("Would you like a photo with it ")
# if wants_photo == "Y":
#     bill += 3
#     print(f"Go ahead and enjoy your bill is {bill}")
# else:
#     print(f"Go ahead and enjoy your bill is {bill}")


# BMI 2.0
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi=round((weight/height**2),2)

# if(bmi < 18.5):
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif(bmi > 18.5 and bmi < 25):
#      print(f"Your BMI is {bmi}, you are normal.")
# elif(bmi > 25 and bmi < 30):
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif(bmi > 30 and bmi < 35):
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# # Leap year check
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # if(year % 4 == 0 and year % 100 != 0 and year % 400 ==0 ):
# #     print("Leap year")
# if(year % 4==0):
#     if(year % 100 ==0):
#         if(year % 400 ==0):
#             print("leap yar")
#         else :
#             print("not a leap year ")
#     else :
#         print("leap year ")
# else :
#     print("not a leap year ")

# # Pizza
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L :")
# add_pepperoni = input("Do you want pepperoni? Y or N :")
# extra_cheese = input("Do you want extra cheese? Y or N :")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill =0
# if(size=='S'):
#      bill=15
#      if(add_pepperoni =='Y'):
#         bill += 2
#         print(bill)
#      else:
#         print(bill)
#         if(extra_cheese=='Y'):
#             bill+=1
#         else:
#             print(bill)
# if(size=='M'):
#      bill=20
#      if(add_pepperoni =='Y'):
#         bill += 3
#         print(bill)
#      else:
#         print(bill)
#         if(extra_cheese=='Y'):
#             bill+=1
#         else:
#             print(bill)
# if(size=='L'):
#      bill=25
#      if(add_pepperoni =='Y'):
#         bill += 3
#         print(bill)
#      else:
#         print(bill)
#         if(extra_cheese=='Y'):
#             bill+=1
#         else:
#             print(bill)

# Solution
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L :")
# add_pepperoni = input("Do you want pepperoni? Y or N :")
# extra_cheese = input("Do you want extra cheese? Y or N :")
# bill =0
# if(size== 'S'):
#     bill+=15
# elif(size=='M'):
#         bill+=20
# elif(size=='L'):
#         bill+=25
# else:s
#     print("Incorrect input")
# if add_pepperoni ==  'Y':
#     if(size=='S'):
#         bill+=2
#     else:
#         bill+=3
# if extra_cheese == 'Y':
#     bill+=1

# print(f"Your final bill is: {bill}")

# Love Calculator
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# combined_name1 = name1 + name2
# name_lower1 = combined_name1.lower()

# count_t = name_lower1.count("t")
# count_r = name_lower1.count("r")
# count_u = name_lower1.count("u")
# count_e = name_lower1.count("e")
# true = count_t + count_r + count_u + count_e
# count_l = name_lower1.count("l")
# count_o = name_lower1.count("o")
# count_v = name_lower1.count("v")
# count_e = name_lower1.count("e")
# love = count_l + count_o + count_v + count_e
# # print(f"T{count_t} R{count_r} U{count_u} E{count_e} L{count_l} O{count_o} V{count_v} E{count_e}")

# love_score = str(true) + str(love)
# print(love_score)
# int_lovescore = int(love_score)
# if int(int_lovescore) < 10 or int_lovescore > 90:
#     print(f"Your score is {int_lovescore}, you go together like coke and mentos")
# elif int_lovescore >= 40 and int_lovescore <= 50:
#     print(f"Your score is {int_lovescore}, you are alright together ")
# else:
#     print(f"Your score is {int_lovescore}")


#Tresure-Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. ") 
step_1=input("You\'re at a cross road.'Where do you want to go? Type 'left' or 'right' :").lower()
if(step_1 == "left"):
    step_2=input('There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim a cross :').lower()
else:
    print("You fell into a hole. Game Over")
if(step_2 == "wait"):
    color=input("You arrive at the island unharmed. There is a house with 3 door . 1.Red , 1.Yellow and 1.Blue . Which colour do you choose? :").lower()
else:
    print("You get attacked by an angry trout. Game Over")
if(color == "red"):
    print("its a room full of fire. Game over")
elif(color=="yellow"):
    print("You found the tresure! You Win!")
elif(color=="blue"):
    print("You enter a room full of beasts. Game Over")
else:
    print("You chose a door that doesn't exist. Game Over.")