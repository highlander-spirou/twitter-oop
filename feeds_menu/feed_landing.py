from __future__ import annotations
from constants import OPTION_MENU, SELECTION_OPTIONS
from helpers import pprint, read_attribute, argmax_dict, compare_tweet_by_timestamp
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from menu_functions import Menu


def feed_landing(self:Menu):
    pprint("Tweet menu")
    current_user = self.get_app.current_user
    option_selection = input(OPTION_MENU["tweet_menu"])
    if int(option_selection) in SELECTION_OPTIONS["tweet_menu"]:
        if int(option_selection) == 1:
            pprint("Here's some feed: ")
            followed = self.get_map.get_following_list(current_user)
            followed_tweets_head = {i: self.get_tweets.get_head_tweet_by_name(i) for i in followed}
            top_10_feeds = compare_tweet_by_timestamp(followed_tweets_head)
            for user, timestamp, id in top_10_feeds:
                pprint(f'{timestamp}: {user} has tweeted "{self.get_tweets.get_tweet_by_id(id).body}" ')
        if int(option_selection) == 2:
            tweet_body = input("\n Share your thoughts: ")
            timestamp = datetime.now()
            self.get_tweets.add_tweet(current_user, tweet_body, timestamp)
        if int(option_selection) == 3:
            pprint("Here's all the tweet that you have posted: ")
            tweets = self.get_tweets.get_tweets_by_name(current_user).traverse_to_n(0, 10)
            tweet_body = [read_attribute(i.data, 'body') for i in tweets]
            tweet_id = [read_attribute(i.data, 'id') for i in tweets]
            for i in zip(tweet_id, tweet_body):
                pprint(': '.join(i))
            

    else:
        pprint('Please enter a valid input between 1 and 4')
        feed_landing(self)
    self.user_menu()