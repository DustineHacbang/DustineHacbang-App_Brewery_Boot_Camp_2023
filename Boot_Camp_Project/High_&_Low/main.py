from art import logo, vs
from game_logic import get_one_rand_celeb, compare_user_val
from game_data import data
import os

score_counter = 0
game_over = False

print(logo)

val_b = get_one_rand_celeb(data)

while game_over == False:

        val_a = val_b
        val_b = get_one_rand_celeb(data)
        print(f"Compare A: {val_a.name}, a {val_a.description} from {val_a.country} ")
        print(f"{val_a.follower_count}")
        
        print(vs)
        
        print(f"Compare B: {val_b.name}, a {val_b.description} from {val_b.country} ")
        print(f"{val_b.follower_count}")
        
        guess = input("Who has more followers? Type 'A' or Type 'B' ").lower()
        
        is_correct = compare_user_val(guess, val_a, val_b)
        # print(test)

        print(logo)
        if is_correct:
            score_counter += 1
            print(f"You're Right! Current Score:{score_counter}.")
        else:
            game_over = True
            print(f"Sorry, That Was Wrong! Final Score {score_counter}.")
