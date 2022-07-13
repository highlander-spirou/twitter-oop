from __future__ import annotations
from getpass import getpass
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from menu_functions import Menu


def login_prompt(self:Menu):
    username = input('Please enter your username: ')
    password = getpass(prompt='Please enter your password: ')
    user = self.get_db.query_user(username, password)
    if user is not None:
        self.get_app.login(username)
        follow_user_set = self.get_map.get_following_list(self.get_app.current_user)
        self.state['initial_followed_tweets_head'] = {i: self.get_tweets.get_tweet_from_user(i) for i in follow_user_set}
        self.user_menu()

    else:
        print('Username or password is invalid, please try again')
        
