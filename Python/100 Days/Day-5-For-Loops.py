# # Py Password Manager
# fruits = ["Apple","Peach","Pear"]
# for fruits in fruits:
#     print(fruits) #Apple , Peach , Pear
#     print(fruits + "Pie") # Apple Pie , Peach Pie , Pear pie

# 🚨 Don't change the code below 👇 ONE Way of doing it 
# from tabnanny import check


# student_heights = input("Input a list of student heights ").split()
# temp1=0
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
  
#   temp= student_heights[n]
#   temp1+= temp 
  
# print(round(temp1/len(student_heights)))

# #Angela Way
# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)): # This loop is to move every data in string to int 
#   student_heights[n] = int(student_heights[n])
# #👆 Integer Data ➡️saved  👆String Data
# # So to get this there is an function already sum() and len() 
# number_of_students=0
# for number in student_heights:
#     number_of_students += 1
# # This will get me the number of students
# height_of_students=0
# for heights in range(0,student_heights):
#     height_of_students += heights

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# check_marks=0
# for marks in student_scores:
#   if(marks> check_marks):
#     check_marks=marks
#   else:
#     continue
# 


# print (check_marks)
# temp=0

# for n in range(0,100):
#     if(n%2==0):
#      temp+=n
# print(temp)


#fizzBuzz Example 
# import random


# for n in range(1,101):
#     if(n%3==0 and n%5==0 ):
#         print("Fizz Buzz")
#     elif(n%3==0):
#         print("Fizz")
#     elif(n%5==0):
#         print("Buzz")
#     else:
#         print(n)

import random
from re import split
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
num_letters=int(input("How many letters would you like in your password: "))
num_symbols=int(input("How many symbols would you like in your password: "))
num_numbers=int(input("How many numbers would you like in your password: "))  # noqa: E999
password=""
# Easy mode
# for char in range(1,num_letters+1):
#     random_char = random.choice(letters)
#     password = password+random_char
 
# for number in range(1,num_numbers+1):
#     random_num = random.choice(numbers)
#     password = password+random_num

# for sym in range(1,num_symbols+1):
#     random_symbols = random.choice(symbols)
#     password = password+random_symbols

# print(password)
# randomizing the content in a string 
# randpass=''.join(random.sample(password,len(password))) #--> Randomizing the content of the a String variable 

# print(randpass)
# Hard mode
password_list=[]
for char in range(1,num_letters+1):
    password_list.append(random.choice(letters))
     
 
for number in range(1,num_numbers+1):
    password_list.append(random.choice(numbers))

for sym in range(1,num_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list) #--> Randomizing the content of the a list 

for char in password_list:
    password+= char
print(password)