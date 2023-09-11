import random
from game_data import data
from game_class import CelebInfo


def get_random_celebrity(data):
    # Generate a random index within the range of the database list
    random_index = random.randint(0, len(data) - 1)
    # Create an instance of the Celebrity class using data from the database
    random_celebrity_data = data[random_index]
    celeb_instance = CelebInfo(
        random_celebrity_data['name'],
        random_celebrity_data['follower_count'],
        random_celebrity_data['description'],
        random_celebrity_data['country']
    )
    return celeb_instance


def get_one_rand_celeb(data):
    return get_random_celebrity(data)


def compare_user_val(guess, val_a, val_b):
    if val_a.follower_count > val_b.follower_count:
        return guess == "a"
    else:
        return guess == "b"