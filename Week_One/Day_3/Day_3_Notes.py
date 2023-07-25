#Control Flow with if/ else and Conditional Operators

#OPERATORS
#> greater than
#>= greater than or equal

#< less than
#<= less than or equal to

#== equal to (checking if equal)
#!= not equal to (checking if its not equal)

#EXAMPLE
print("Welcome to the rollercoaster!")
hieght = int(input("What is yout hieght incm?"))

if hieght >= 120:
    print("you can ride the rollercoaster!")
else:
        print("Sorry, you have to grow taller before you can ride.")
# -----------------------------------------------------------------------

#CONDITIONAL NESTED STATEMENTS
# *Example*
# if condition:
#     do this
# els:
#     do this

# *EXAMPLE*
print("Welcome to the rollercoaster!")
hieght = int(input("What is yout hieght incm?"))

if hieght >= 120:
    print("you can ride the rollercoaster!")
    #NESTED Condition
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    #elsif statements can be added as many times you need to
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
        print("Sorry, you have to grow taller before you can ride.")

# Multi. if statments
#Continues conditions
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

# if/elsif/else
# 1 condition not continues
#     if condition1:
#         do A 
#     if condition2:
#         do B
#     else:
#         do C

#Example
print("Welcome to the rollercoaster!")
hieght = int(input("What is yout hieght incm?"))

bill = 0

if hieght >= 120:
    print("you can ride the rollercoaster!")
    #NESTED Condition
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    #elsif statements can be added as many times you need to
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    wants_pohoto = input("Do you want a photo taken? Y or N")
    if wants_pohoto == "Y":
        #add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# #Combining multi. conditions in 1 conditition
# if condition1 & condition2 & contition3:
#     do this
# else:
#     do this

# Logical Operator

# " and " both condition needs to be true
# " or " at least one of them needs to be true
# " not " reverses a condition if its true originally then it will become false

print("Welcome to the rollercoaster!")
hieght = int(input("What is yout hieght incm?"))

bill = 0

if hieght >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <55:
        print("Everything is ok the tickets on us")
    else:
        bill = 12
        print("Please pay $12.")
    wants_pohoto = input("Do you want a photo taken? Y or N")
    if wants_pohoto == "Y":
        bill += 3
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
