import random
import string

def create_random():
    strings = list(string.ascii_letters + string.digits)
    random_str = []
    for i in range(8):
        random_str.append(random.choice(strings))
    return "".join(random_str)