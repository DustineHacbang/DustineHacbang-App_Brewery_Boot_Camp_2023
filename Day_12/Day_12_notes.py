
################### Scope ####################

#Scope Def: The scope of a variable is the region of your program in which it is defined.



#example
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope: variables defined within a function

#example

def drink_potion(): #local scope for potion_strength is within the function
    potion_strength = 2
    print(potion_strength)

drink_potion()  
# print(potion_strength) #this will not work because potion_strength is not defined outside of the function

#globa scope: variables defined outside of a function

player_health = 10 #global scope for player_health is outside of the function

def game():
    def drink_potion():    #this will work because potion_strength is defined within the function
        potion_strength = 2
        print(player_health)

    drink_potion () #this will work because potion_strength is defined within the function

# There is no block scope in python

#example
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) #this will work because new_enemy is defined outside of the if statement

#Modifying Global Scope

enemies = 1

def increase_enemies():
    #you do not need to define a global variable if you are only accessing it
    #it will confuse the program if you define a global variable and a local variable with the same name
    global enemies #this will allow the function to modify the global variable
    enemies = "Zombies"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

##########################################

def increase_enemies():
    #
    return enemies + 1 #this will return the value of enemies + 1 and will

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants are always in all caps
#example
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"