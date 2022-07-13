from getpass import getpass
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from Twitter import Twitter, LoginDb, FollowMap, TweetDatabase
from sign_in_methods.menu_landing import menu_landing
from sign_in_methods.login_prompt import login_prompt
from sign_in_methods.follow_menu import follow_menu
from feeds_menu.feed_landing import feed_landing
from feeds_menu.feed_function import render_tweets
from helpers import register_method, pprint, BaseClass
from interfaces import ObserverInterface

class MenuWrapper:
    def __init__(self, app:Twitter, login_db:LoginDb, follow_map:FollowMap, tweet_list:TweetDatabase) -> None:
        self.__app = app
        self.__login_db = login_db
        self.__follow_map = follow_map
        self.__tweet_list = tweet_list

    @property
    def get_app(self):
        return self.__app
    @property
    def get_db(self):
        return self.__login_db
    @property
    def get_map(self):
        return self.__follow_map
    @property
    def get_tweets(self):
        return self.__tweet_list


@register_method((menu_landing, login_prompt, follow_menu, feed_landing))
class Menu(MenuWrapper, metaclass=BaseClass):
    def __init__(self, app:Twitter, login_db:LoginDb, follow_map:FollowMap, tweet_list:TweetDatabase) -> None:
        super().__init__(app, login_db, follow_map, tweet_list)
    
    def __post_init__(self):
        self.state:ObserverInterface = {
                'current_user': self.get_app,
                'tweet_db': self.get_tweets,
                'follow_map': self.get_map,
                'initial_primer': None,
                'initial_followed_tweets_head': None
            }
    
    def sign_up_menu(self): 
        pprint('You are in sign up menu')
        username = input('Please enter your username: ')
        password = getpass(prompt='Please enter your password: ')
        self.__login_db.create_user(username, password)
    
    
    def user_menu(self):
        while True:
            current_user = self.get_app.current_user
            if current_user is None:
                self.login_prompt()
            else:
                pprint(f'Welcome {current_user}')
                option_selection = input('\n ------ \n' + OPTION_MENU['login'])
                try:
                    if int(option_selection) in SELECTION_OPTIONS['login']:
                        if int(option_selection) == 1:
                            self.feed_landing()
                        elif int(option_selection) == 2:
                            self.follow_menu()
                        elif int(option_selection) == 3:
                            pprint("Change password menu")
                            old_password = getpass(prompt='Please enter your old password: ')
                            result = self.__login_db.change_password(current_user, old_password)
                            if result is True:
                                self.__app.logout()
                        elif int(option_selection) == 4:
                            self.__app.logout()
                    else:
                        raise InvalidInput(option_selection)
                except InvalidInput as e:
                    print(e.message)
                except ValueError:
                    pprint('Please type a number between 1 and 4')

