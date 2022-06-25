from getpass import getpass
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from Twitter import Twitter, LoginDb

class Menu:
    def __init__(self, app:Twitter, login_db:LoginDb) -> None:
        self.__app = app
        self.__login_db = login_db
        
    
    def sign_up_menu(self): 
        print('You are in sign up menu')
        username = input('Please enter your username: ')
        password = getpass(prompt='Please enter your password: ')
        self.__login_db.create_user(username, password)
    
    
    def sign_in_menu(self):
        if self.__app.login_state is False:
            username = input('Please enter your username: ')
            password = getpass(prompt='Please enter your password: ')
            user = self.__login_db.query_user(username, password)
            if user is None:
                print('Username or password is invalid, please try again')
            else:
                self.__app.login(username)
                self.sign_in_menu()
        else:
            option_selection = input(OPTION_MENU['login'])
            try:
                if int(option_selection) in SELECTION_OPTIONS['login']:
                    if int(option_selection) == 1:
                        print("Latest feeds")
                        return 
                    elif int(option_selection) == 2:
                        print("Following list")
                    elif int(option_selection) == 3:
                        print("Follower list")
                    elif int(option_selection) == 4:
                        print("Change password menu")
                        old_password = getpass(prompt='Please enter your old password: ')
                        result = self.__login_db.change_password(self.__app.login_state, old_password)
                        if result is True:
                            self.__app.logout()
                    elif int(option_selection) == 5:
                        return
                else:
                    raise InvalidInput(option_selection)
            except InvalidInput as e:
                print(e.message)
            except ValueError:
                print('Please type a number between 1 and 5')
                