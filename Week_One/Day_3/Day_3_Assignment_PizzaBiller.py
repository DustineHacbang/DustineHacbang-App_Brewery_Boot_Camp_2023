# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

sp = size
ap = add_pepperoni
ec = extra_cheese
total_bill = 0

if size == "S":
    total_bill += 15
    if ap == "Y":
        total_bill += 2
    if ec == "Y":
        total_bill +=1
if size == "M":
    total_bill += 20
    if ap == "Y":
        total_bill += 3
    if ec == "Y":
        total_bill +=1
if size == "L": 
    total_bill += 25
    if ec == "Y": 
        total_bill +=1
print(f"Your final bill is: ${total_bill}.")