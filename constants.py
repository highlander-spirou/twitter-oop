from typing import TypedDict

class OptionMenu(TypedDict):
    welcome:str
    login:str
    follow:str
    follower:str
    
class SelectionOptions(TypedDict):
    welcome:list
    login:list
    follow:list
    follower:str


OPTION_MENU: OptionMenu = {
    'welcome': """
Type the number to:
1. Sign Up
2. Sign In
3. Log out (end the program)
You are typing: """,
    'login': """
Type the number to:
1. View feeds
2. View follow menu
3. Depricated
4. Change password
5. Log out (Return to main menu)
You are typing: """,
    'follow': """
Type the number to:
1. View Follower
2. View Following
3. Go back
You are typing: """,
    'follower': """
Type the number to:
1. Follow User
2. Unfollow User
3. Go back
You are typing: """,
}

SELECTION_OPTIONS: SelectionOptions = {
    'welcome': [1,2,3],
    'login': [1,2,3,4,5],
    'follow': [1,2,3],
    'follower': [1,2,3],
}