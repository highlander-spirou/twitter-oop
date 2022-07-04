from __future__ import annotations
from copy import deepcopy
import random
import string
from typing import Dict, Union, TYPE_CHECKING, Any
from collections import OrderedDict

if TYPE_CHECKING:
    from Twitter import TweetNode

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
    f = lambda i: li[i]
    re = max(range(len(li)), key=f)
    return re

def argmax_dict(d: dict) -> tuple:
    return max(d.items(), key = lambda k : k[1])

def get_last_ordered_dict(o_dict:OrderedDict):
    return next(reversed(o_dict))

def compare_tweet_by_timestamp(d:Dict[str, TweetNode], num_compare = 10):
    """
    Compare in num_compare*len(linked_list) time complexity. 
    To reduce the runtime to n*log(n), use MinHeap datastructure retrieve the ordered list by HeapSort
    """
    re = []
    i = 0
    while i < num_compare:
        d1 = {}
        for index, value in d.items():
            d1[index] = value.get_timestamp_id()

        max_index = argmax_dict(d1)[0]
        re.append((max_index, d[max_index].get_timestamp_id(), d[max_index].get_timestamp_id('id')))
        d[max_index] = d[max_index].next_node
        i += 1
    return re
