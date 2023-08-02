#FUNCTIONS#
#group of for loop,while loops, etc..#


def my_function():
    #Do_this
    #Then do this
    #Finally do this
    pass


#EXAMPLE#
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()


#Variables can be passed in the functions just like the "something" in the examply#
def my_function(something):
    #Do_this with "somtehing"
    #Then do this
    #Finally do this
    pass


#EXAMPLE
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")

greet_with_name("Dustine")

#Function with inputs#

#Parameter is "something"
#Argument is "123"

something = 123

def my_function(something):
    #Do_this with "somtehing"
    #Then do this
    #Finally do this
    pass

my_function(123)


#Function with Multiple inputs

#Example

def greet_with(name,location):
    print(f'Hello {names}')
    print(f'What is it like {location}')
    
greet_with("Jack","England")

#__________________________________________________________________

#this is call positional argument meaning based on the location in which you pass the variable#
#the code will pull it by where it was placed.

#Example england and jack was flipped  and put in the wrong location 
greet_with("England","Jack")

#___________________________________________________________________

#Key word arguments meaning the arguments are defined regardless with the order

#Example

greet_with(location="England",name="Jack")