import random
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=[rock, paper,scissors]

ai_choice = random.choice(options)


user = input("What do you choose? 0 for Rock, 1 for Paper, or 2 for Sicssors.")
user_choice= options[int(user)]

print("User's Choice")
print(user_choice)
print("Opponent's Choice")
print(ai_choice)

if user_choice < ai_choice:
    if user_choice == rock and ai_choice == scissors:
        print("You Lose")
    else:
        print("You Win")

elif user_choice == ai_choice:
    print("Draw")

else:
    if user_choice == scissors and ai_choice == rock:
        print("You Win")
    else:
        print("You Lose")