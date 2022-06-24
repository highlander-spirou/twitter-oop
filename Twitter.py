import random
import string
from getpass import getpass

def create_random():
    strings = list(string.ascii_letters + string.digits)
    password = []
    for i in range(8):
        password.append(random.choice(strings))
    return "".join(password)

class Database:
    def __init__(self) -> None:
        self.db = []
        
    


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.id = create_random()
        self.password = password
        
    def welcome_statement(self):
        print(f'Create new user {self.username} with ID: {self.id}')
        
    

def postTweet(userID, tweetBody):
    pass

def getNewFeed():
    pass

def follow():
    pass

def unfollow():
    pass


class InvalidInput(Exception):
    def __init__(self, input) -> None:
        self.input = input
        self.message = f'{input} is not a valid input, please between 1 to 3'
        super().__init__(self.message)

OPTIONS_RANGE = [1, 2, 3]
IS_CONTINUE = True
option_statement = """
    Type the number to:
    1. Sign Up
    2. Sign In
    3. Log out (end the program)
    You are typing: 
"""

def sign_up_user(username, password):
    new_user = User(username, password)
    new_user.welcome_statement()
    return new_user

def run_program():
    while True:
        option_selection = input(option_statement)
        try:
            if int(option_selection) in OPTIONS_RANGE:
                if int(option_selection) == 1:
                    print('You are in sign up menu')
                    username = input('Please enter your username: ')
                    password = getpass(prompt='Please enter your password: ')
                    sign_up_user(username, password)
                    break
                if int(option_selection) == 2:
                    username = input('Please enter your username: ')
                    password = getpass(prompt='Please enter your password: ')
                    print(username, password)
                if int(option_selection) == 3:
                    global IS_CONTINUE
                    IS_CONTINUE = False
                    break
            else:
                raise InvalidInput(option_selection)
        except InvalidInput as e:
            print(e.message)
        except ValueError:
            print('Please type a number between 1 and 3')
        
    
    
if __name__ == '__main__':
    Quit = input('Welcome to Twitter 🐦 \n Press Enter to continue \n Press Q to Quit')
    while Quit != "q" and IS_CONTINUE:
        run_program()