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
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
gameover = "false"

stage_one = input("Left or Right? ")
stage_one = stage_one.lower()

if stage_one == "left":
    gameover = "true"
    print("Game Over")    
else:
    print("Proceed to next stage!")

if gameover == "false":
    stage_two = input("Wait or Swim? ")
    stage_two = stage_two.lower()

    if stage_two == "swim":
        gameover = "true"
        print("Game Over")
    else:
        print("Proceed to next stage!")

if gameover == "false":
    stage_three = input("Which door do you chose? Blue, Red, Orange, Yellow? ")
    stage_three = stage_three.lower()

    if stage_three == "Blue":
        gameover = "true"
        print("Game Over... Death by Drowning")
    elif stage_three == "red":
        gameover = "true"
        print("Game Over... Death by Fire")
    elif stage_three == "orange":
        gameover = "true"
        print("Game Over... Death by pumkins")
    else:
        print("Congrats you have reached the One Piece!!")
