# print("Welcome to the RollerCoster")
# height = int(input("Enter your height in cms :"))

# if height >= 120:
#     print("Go ahead and enjoy")
# else:
#     print("Sorry you need to grow up") 

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

# Pizza 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill =0
if(size=='S'):
     bill=15
     if(add_pepperoni =='Y'):
        bill += 2
        print(bill)
     else:
        print(bill)
        if(extra_cheese=='Y'):
            bill+=1
        else:
            print(bill)
if(size=='M'):
     bill=20
     if(add_pepperoni =='Y'):
        bill += 3
        print(bill)
     else:
        print(bill)
        if(extra_cheese=='Y'):
            bill+=1
        else:
            print(bill)
if(size=='L'):
     bill=25
     if(add_pepperoni =='Y'):
        bill += 3
        print(bill)
     else:
        print(bill)
        if(extra_cheese=='Y'):
            bill+=1
        else:
            print(bill)
