from __future__ import annotations
from constants import OPTION_MENU, SELECTION_OPTIONS
from helpers import pprint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from menu_functions import Menu



def follower_menu(self:Menu, current_user):
    print("\nFollowing list: ", self.get_map.get_following_list(current_user))
    option_selection = input(OPTION_MENU['follower'])
    if int(option_selection) in SELECTION_OPTIONS['follower']:
        if int(option_selection) == 1:
            user = input('Please type the username to follow: ')
            if self.get_db.search_username(user) is True:
                self.get_map.add_follow(current_user, user)
                pprint(f'✔ Follow user {user}')
            else:
                pprint(f'User {user} does not exists, please try a valid username')
            follower_menu(self, current_user)
        elif int(option_selection) == 2:
            user = input('Please type the username to unfollow: ')
            self.get_map.unfollow_user(current_user, user)
            follower_menu(self, current_user)
        elif int(option_selection) == 3:
            follow_menu(self)
    else:
        pprint('Please input between 1 and 3')

def followee_menu(self, current_user):
    pprint("Follower list")
    pprint(f'Your Follower list: {self.get_map.get_follower_list(current_user, "str")} \n')
    follow_menu(self)

def follow_menu(self):
    current_user = self.get_app.current_user
    option_selection = input(OPTION_MENU['follow'])
    if int(option_selection) in SELECTION_OPTIONS['follow']:
        if int(option_selection) == 1:
            follower_menu(self, current_user)
        elif int(option_selection) == 2:
            followee_menu(self, current_user)
    else:
        pprint('Please input between 1 and 3')

