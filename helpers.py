from __future__ import annotations
import random
import string
from typing import Dict, Union, TYPE_CHECKING, Any
from collections import OrderedDict

if TYPE_CHECKING:
    from data_structures.Stack import Stack 

def create_random():
    strings = list(string.ascii_letters + string.digits)
    random_str = []
    for i in range(8):
        random_str.append(random.choice(strings))
    return "".join(random_str)


def register_method(functions:Union[Any, tuple]):
    def decorator(Class):
        if isinstance(functions, tuple):
            for function in functions:
                setattr(Class, function.__name__, function)
            return Class
        else:
            setattr(Class, functions.__name__, functions)
            return Class
    return decorator


def pprint(text:str):
    """
    Add extra padding to print function
    """
    print("\n " + text + "\n")


def extract_dict_values(d:dict):
    return next(iter(d.values()))

def extract_dict_keys(d:dict):
    return next(iter(d.keys()))


def read_attribute(d:dict, attr):
    extracted_value = extract_dict_values(d)
    if type(extracted_value) != 'dict':
        return getattr(extracted_value, attr)
    else:
        return extracted_value[attr]


def argmax(li:list) -> int:
    """
    This function returns index of max item in an iterator
    """
    f = lambda i: li[i] # this returns value at index i
    re = max(range(len(li)), key=f) 
    return re

def argmax_dict(d: dict) -> str:
    """
    This function returns the key of which value is the highest
    """
    # {'a': 1, 'b': 2} -> returns { 'a':1 }
    # for key extraction, uses d.keys()
    # for value extraction, uses d.values()
    return max(d.keys(), key = lambda k : k[1])





class BaseClass(type):
    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.__post_init__()
        return obj