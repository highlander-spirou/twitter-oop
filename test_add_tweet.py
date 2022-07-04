from datetime import datetime
from random import randrange
from datetime import timedelta, datetime
import random

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def create_random_date():
    d1 = datetime.strptime('1/6/2022 1:00 AM', '%d/%m/%Y %I:%M %p')
    d2 = datetime.strptime('30/7/2022 11:59 PM', '%d/%m/%Y %I:%M %p')
    return random_date(d1, d2)

def create_random_range(num_range):
    re = []
    for i in range(num_range):
        re.append(create_random_date())

    return sorted(re)



def create_tweets(tweet_list, num_tweet=20, user_range=None):
    random_datetime = create_random_range(num_tweet)

    if user_range is None:
        for i in range(num_tweet):
            random_user = random.randint(0, 2)
            if random_user == 0:
                tweet_list.create_tweet('nhan', f'Tweet from Nhan {i}', random_datetime.pop(0))
            elif random_user == 1:
                tweet_list.create_tweet('nhu', f'Như has complaint {i}th time', random_datetime.pop(0))
            else:
                tweet_list.create_tweet('map', f'Mập nói "mập sang mập đẹp {i} times"', random_datetime.pop(0))
    else:
        for i in range(num_tweet):
            random_user = random.randint(0, user_range)
            if random_user == 0:
                tweet_list.create_tweet('nhan', f'Tweet from Nhan {i}', random_datetime.pop(0))
            elif random_user == 1:
                tweet_list.create_tweet('nhu', f'Như has complaint {i}th time', random_datetime.pop(0))
            elif random_user == 2:
                tweet_list.create_tweet('map', f'Mập nói "mập sang mập đẹp {i} times"', random_datetime.pop(0))
            else:
                tweet_list.create_tweet(f'user{random_user}', f'user{random_user} is saying {i}', random_datetime.pop(0))

    