from __future__ import annotations
from copy import copy
from interfaces import ObserverInterface
from helpers import argmax_dict, pprint, extract_dict_values
from typing import TYPE_CHECKING, Dict
from data_structures.Stack import Stack

if TYPE_CHECKING:
    from Twitter import TweetDatabase

def compare_tweet_by_timestamp(d:Dict[str, Stack], tweet_db:TweetDatabase, num_compare = 10):
    """
    Compare in num_compare*len(following_map) time complexity. 
    To reduce the runtime to n*log(n), use MinHeap datastructure retrieve the ordered list by HeapSort
    """
    
    re = []
    i = 0
    if isinstance(extract_dict_values(d), Stack):
        d1 = {key: d[key].head for key in d.keys() if d[key] is not None}
    else:
        d1 = d
    while i < num_compare:
        if len(d1) != 0: 
            d1_id = {key: d1[key].data for key in d1.keys()}
            d1_tweet_timestamp = {key: tweet_db.get_tweet_from_id(d1_id[key]).timestamp for key in d1_id.keys()}
            max_index = argmax_dict(d1_tweet_timestamp)
            re.append(d1_id[max_index])
            if d1[max_index].next_node is None:
                d1.pop(max_index)
            else:
                d1[max_index] = d1[max_index].next_node

            i+=1
        else:
            break
    return d1, re

def view_feeds(observer_state:ObserverInterface):
    copied_state = copy(observer_state)
    if copied_state['current_user'].current_user is not None:
        # follow_user_set = copied_state['follow_map'].get_following_list(copied_state['current_user'].current_user)
        # followed_tweets_head = {i: copied_state['tweet_db'].get_tweet_from_user(i) for i in follow_user_set}
        old_state, top_10_tweet = compare_tweet_by_timestamp(copied_state['initial_followed_tweets_head'], copied_state['tweet_db'])
        for i in top_10_tweet:
                tweet = copied_state['tweet_db'].get_tweet_from_id(i)
                tweet_rendered_body = f'{tweet.timestamp} - {tweet.owner}: "{tweet.body}"'
                pprint(tweet_rendered_body)
        while len(old_state) != 0:
            copied_state['initial_followed_tweets_head'] = old_state
            quit_observing = input('Press "n" to get more tweets, "q" to quit')
            if quit_observing == "q":
                print('quit')
            elif quit_observing == 'n':
                print('continue')
                view_feeds(copied_state)
            else:
                print('wrong input')
