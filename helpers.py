import random
import string
from typing import Union
def create_random():
    strings = list(string.ascii_letters + string.digits)
    random_str = []
    for i in range(8):
        random_str.append(random.choice(strings))
    return "".join(random_str)


def register_method(functions:Union[callable, tuple]):
    def decorator(Class):
        if isinstance(functions, tuple):
            for function in functions:
                setattr(Class, function.__name__, function)
            return Class
        else:
            setattr(Class, functions.__name__, functions)
            return Class
    return decorator