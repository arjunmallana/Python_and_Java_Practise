#  # Data Types

# #String

# print("Hello"[0])
# # print("String" [String_index])
# # Output : H
# print("Hello"[1])
# # print("String" [String_index])
# # Output : e
# print("Hello"[2])
# # print("String" [String_index])
# # Output : l
# print("Hello"[3])
# # print("String" [String_index])
# # Output : l
# print("Hello"[4])
# # print("String" [String_index])
# # Output : o
# print("123"+"345" )
# # String concantanation
# # Output: 123345

# # Integer

# print(123+345)
# # Output : 468
# # 123,456,789 can be written as 123_456_789
# print(123_456_789+123_456_789)
# # Output : 246913578

# # Float
# # 3.14159

# # Boolean 
#     # True or False
#     # 1    or 0

# # l = [1,2,3]+[1,1,1]
# # print(l)

# # # 🚨 Don't change the code below 👇
# # two_digit_number = input("Type a two digit number: ")
# # # 🚨 Don't change the code above 👆

# # ####################################
# # #Write your code below this line 👇
# # a = two_digit_number[0]
# # b = two_digit_number[1]

# # print(int(a)+int(b))
# height = 1.75
# weight = 80
# print(weight +' ÷ '+ height +' X '+ height +' = ')
# round(number,ndigits)
print(round(8 / 3,2))

# (//) flow division
print(8//3)

# # Life Remaining 
# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# age_int= int(age)
# year_remain = 90-age_int
# days_remaning = year_remain * 365
# weeks_remaing = year_remain * 52
# months_remaning = year_remain * 12 


# print(f"You have {days_remaning} days, {weeks_remaing} weeks, and {months_
# remaning} months left.")


# Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling 
# to solve this.💪

#Write your code below this line 👇
###1###
# print("Welcome to Tip Calculator. ")
# total_bill = input("Enter the Total Bill: ")
# tip=input("Enter the percentage of the tip: ")
# ppl = input("Enter how many people the bill is spl: ")
# # result = ((float(total_bill)/float(ppl))*float(tip)/100)
# result_ppl = round(float(total_bill)/float(ppl),2)
# result_ppl += (float(tip)/100) * result_ppl
# print(f"each person should pay:$ {result_ppl}")
# ###2###
# print("Welcome to Tip Calculator. ")
# bill = float(input("Enter the Total Bill: "))
# tip=int(input("Enter the percentage of the tip: "))
# ppl = int(input("Enter how many people the bill is spl: "))
# tip_percent=tip/100
# total_tip_amount = bill*(tip_percent)
# total_bill_amount = bill + total_tip_amount
# bill_per_person = total_bill_amount/ppl
# final_amount=round(bill_per_person,2)  #output .0 we get it is one decimal 
# place not 
# two due to a format issue to tackle that we have next function
# final_amount="{.2f}".format(bill_per_person) #output .00 
# print(f"Each person should pay $ {final_amount}")