from typing import TypedDict

class OptionMenu(TypedDict):
    welcome:str
    login:str
    following:str
    
class SelectionOptions(TypedDict):
    welcome:list
    login:list
    following:list


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
2. View followers
3. View followee
4. Change password
5. Log out (Return to main menu)
You are typing: """,
    'following': """
Type the number to:
1. Follow a user
2. Unfollow a user
3. Go back
You are typing: """,
}

SELECTION_OPTIONS: SelectionOptions = {
    'welcome': [1,2,3],
    'login': [1,2,3,4,5],
    'following': [1,2,3]
}