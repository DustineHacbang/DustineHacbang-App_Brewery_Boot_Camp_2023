

def guess(random_num, guess_counter):
    while guess_counter != 0:
        guess = input("Make a guess: ")
        if int(guess) == random_num:
            guess_counter = 0
            print(f"You Got It! The Answer Was {guess}")
        else:
            guess_counter -= 1
            if guess_counter != 0:
                print("Try Again")
                if int(guess) < int(random_num):
                    print("Too Low ")
                else:
                    print("To High")
            if guess_counter == 0:
                print("You Lose Try Again")