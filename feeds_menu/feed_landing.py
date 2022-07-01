from __future__ import annotations
from constants import OPTION_MENU, SELECTION_OPTIONS
from helpers import pprint
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from menu_functions import Menu


def feed_landing(self:Menu):
    pprint("Tweet menu")
    option_selection = input(OPTION_MENU["tweet_menu"])
    if int(option_selection) in SELECTION_OPTIONS["tweet_menu"]:
        if int(option_selection) == 1:
            pprint("Here's some feed: ")
            pprint(self.get_tweets.get_tweets_by_name(self.get_app.current_user))
        if int(option_selection) == 2:
            tweet_body = input("\n Share your thoughts: ")
            timestamp = datetime(2022, 7,1,0,13)
            self.get_tweets.add_tweet(self.get_app.current_user, tweet_body, timestamp)

        if int(option_selection) == 3:
            pprint("Here's all the tweet that you have posted")
    else:
        pprint('Please enter a valid input between 1 and 4')
        feed_landing(self)
    self.user_menu()