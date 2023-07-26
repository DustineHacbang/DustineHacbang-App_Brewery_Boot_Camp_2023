# *******For Loops*******

# for item in list of them:
# #Do somthing with this list

fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit +" Pie")

# -------------------------------
#FOR LOOP WITH RANGE FUNCTION

#EXAMPLE
# for number in range(a,b):
#     print(number)

#it will only print 0-9
for number in range(1,10):
    print(number)

#it will only print 0-10
for number in range(1,11):
    print(number)

#range(x starting point, y end point, z incrimints)

#this will start at 1 going to 10 by 3s
range(1,11,3)

#EXAMPLE
#Will add all numbers  from 1-100 equaling to 5050
total=0
for number in range(1,101):
    total+= number
print(total)
