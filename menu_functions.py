from getpass import getpass
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from Twitter import Twitter, LoginDb, FollowMap
from sign_in_methods.landing import landing_page
from sign_in_methods.login_prompt import login_prompt
from sign_in_methods.follow_menu import follow_menu
from helpers import register_method

class MenuWrapper:
    def __init__(self, app:Twitter, login_db:LoginDb, follow_map:FollowMap) -> None:
        self.__app = app
        self.__login_db = login_db
        self.__follow_map = follow_map

    @property
    def get_app(self):
        return self.__app
    @property
    def get_db(self):
        return self.__login_db
    @property
    def get_map(self):
        return self.__follow_map


@register_method((landing_page, login_prompt, follow_menu))
class Menu(MenuWrapper):
    def __init__(self, app: Twitter, login_db: LoginDb, follow_map: FollowMap) -> None:
        super().__init__(app, login_db, follow_map)
    
    
    def sign_up_menu(self): 
        print('You are in sign up menu')
        username = input('Please enter your username: ')
        password = getpass(prompt='Please enter your password: ')
        self.__login_db.create_user(username, password)
    
    
    def sign_in_menu(self):
        while True:
            current_user = self.get_app.current_user
            if current_user is None:
                self.login_prompt()
            else:
                print(f'\n Welcome {current_user}')
                option_selection = input('\n ------ \n' + OPTION_MENU['login'])
                try:
                    if int(option_selection) in SELECTION_OPTIONS['login']:
                        if int(option_selection) == 1:
                            print("\n \n Latest feeds")
                            return 
                        elif int(option_selection) == 2:
                            self.follow_menu()
                        elif int(option_selection) == 3:
                            print("Depricated")
                        elif int(option_selection) == 4:
                            print("Change password menu")
                            old_password = getpass(prompt='Please enter your old password: ')
                            result = self.__login_db.change_password(current_user, old_password)
                            if result is True:
                                self.__app.logout()
                        elif int(option_selection) == 5:
                            self.__app.logout()
                    else:
                        raise InvalidInput(option_selection)
                except InvalidInput as e:
                    print(e.message)
                except ValueError:
                    print('Please type a number between 1 and 5')
                