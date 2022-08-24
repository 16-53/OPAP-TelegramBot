import random


def random_n():
    numbers = sorted(random.sample(range(1, 46), 5))
    number = random.randrange(1, 21)

    return numbers, number
