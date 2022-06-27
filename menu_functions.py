from getpass import getpass
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from Twitter import Twitter, LoginDb, FollowMap

class Menu:
    def __init__(self, app:Twitter, login_db:LoginDb, follow_map:FollowMap) -> None:
        self.__app = app
        self.__login_db = login_db
        self.__follow_map = follow_map
    
    def landing_page(self):
        if self.__app.current_user is None:
            option_selection = input(OPTION_MENU['welcome'])
            try:
                if int(option_selection) in SELECTION_OPTIONS['welcome']:
                    if int(option_selection) == 1:
                        self.sign_up_menu()
                    if int(option_selection) == 2:
                        self.sign_in_menu()
                    if int(option_selection) == 3:
                        return False
                else:
                    raise InvalidInput(option_selection)
            except InvalidInput as e:
                print(e.message)
            except ValueError:
                print('Please type a number between 1 and 3')
        else:
            self.sign_in_menu()
    
    def sign_up_menu(self): 
        print('You are in sign up menu')
        username = input('Please enter your username: ')
        password = getpass(prompt='Please enter your password: ')
        self.__login_db.create_user(username, password)
    
    
    def sign_in_menu(self):
        while True:
            current_user = self.__app.current_user
            if current_user is None:
                username = input('Please enter your username: ')
                password = getpass(prompt='Please enter your password: ')
                user = self.__login_db.query_user(username, password)
                if user is None:
                    print('Username or password is invalid, please try again')
                else:
                    self.__app.login(username)
                    self.sign_in_menu()
            else:
                print(f'Welcome {current_user}')
                option_selection = input(OPTION_MENU['login'])
                try:
                    if int(option_selection) in SELECTION_OPTIONS['login']:
                        if int(option_selection) == 1:
                            print("Latest feeds")
                            return 
                        elif int(option_selection) == 2:
                            print("Following list")
                            print(self.__follow_map.get_following_list(current_user))
                            option_selection = input(OPTION_MENU['following'])
                            if int(option_selection) == 1:
                                user = input('Please type the username to follow: ')
                                if self.__login_db.search_username(user) is True:
                                    self.__follow_map.add_follow(current_user, user)
                                    print(f'✔ Follow user {user} ')
                                else:
                                    print(f'User {user} does not exists, please try a valid username')
                                    
                        elif int(option_selection) == 3:
                            print("Follower list")
                            print(f'Your Follower list: {self.__follow_map.get_follower_list(current_user, "str")}')
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
                