from getpass import getpass

class Twitter:
    def __init__(self) -> None:
        self.__login_state = False
        self.__current_user = None
    
    @property
    def login_state(self):
        return self.__login_state
    
    @property
    def current_user(self):
        return self.__current_user
    
    @current_user.setter
    def set_current_user(self, user):
        self.__current_user = user
    
    def login(self, username):
        self.__login_state = username
        
    def logout(self):
        self.__login_state = False
        
        

class User:
    def __init__(self) -> None:
        pass
        
    

class LoginDb:
    def __init__(self) -> None:
        self.__users = {}
    
    def create_user(self, username, password):
        if self.search_username(username) is False:
            new_user = User()
            print(f'Create new user {username}')
            self.add_user(username, password, new_user)
        else:
            print('This username has been taken, please use another username')
     
    def search_username(self, username:str) -> bool:
        keys = [i[0] for i in self.__users.keys()]
        if username in keys:
            return True
        else:
            return False
    
    def add_user(self, username, password, user:User):
        self.__users[(username, password)] = user
        
    def query_user(self, username, password):
        try:
            return self.__users[(username, password)]
        except Exception:
            return None
        
    def change_password(self, username, old_password):
        user_obj = self.query_user(username, old_password)
        if user_obj is not None:
            new_password = getpass(prompt='Please enter your new password: ')
            self.__users.pop((username, old_password))
            self.add_user(username, new_password, user_obj)
            print('Successfully reset your password')
            return True
        else:
            print('Incorrect old password, please try again')
            return False
        





def postTweet(userID, tweetBody):
    pass

def getNewFeed():
    pass

def follow():
    pass

def unfollow():
    pass
