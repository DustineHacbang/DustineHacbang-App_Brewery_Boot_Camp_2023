# Randimizor

import random
import my_module
# print(my_module.pi)

random_integar = random.radiant(1,10)
print( random_integar)


random_float = random.random()

#this code increases the random num from between 0-1 now from 0-5
random_float * 5

print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
#------------------------------------------------------------------------------------------
#Python List Data Structure

#Data has that has relationships with each other.

#Example 1
state_of_america =["California","Texas", "Arizon","Florida"]

#this should print california
print(state_of_america[0])

#this will change the value in the list
state_of_america[2]= "Arizona Tea"

#append will allow us to add an item to the list
state_of_america.append("Washington")

#.extend will allow us to add another list to the list
state_of_america.extend(["Iowa","Illinoi"])

#Example 2
fruits =["Apple","Orange","Paer"]

#index out of range error will be recived due to  counting will start in 0 so
# when there is 50 state the last state will be in index 49 due to programing starts at 0 not 1

num_of_state = len(state_of_america)

#"-1" will prevent the index error so you can pull the last item from the list
print(state_of_america - 1)

