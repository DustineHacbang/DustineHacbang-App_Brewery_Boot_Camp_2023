#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from function import guess

import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_num = random.randint(1, 100)
print(f"Pssst, the correct answer is {random_num}")

difficulty = ""
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guess_counter = 10
    guess(random_num, guess_counter)


if difficulty == "hard":
    guess_counter = 5
    guess(random_num, guess_counter)