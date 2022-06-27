from getpass import getpass
from dataclasses import dataclass, field
from typing import List, Literal, Tuple
from helpers import create_random
from Graph import Graph, Edge

  
class Tweets:
    pass
      
@dataclass
class TweetsList:
    __tweets_list:List[Tuple[str, str, Tweets]] = field(default_factory=list)
    
    def get_tweets_by_user_name(self, username):
        re = [i[1] for i in self.__tweets_list if i[1] == username]
        return re
    
    def queue_to_tweet_list(self, username, tweets:Tweets):
        tweet_id = create_random()
        pass
    
 
class FollowMap:
    def __init__(self) -> None:
        self.__follow_map = Graph()
        
    def add_follow(self, followee, follower):
          self.__follow_map.add_edge(Edge((followee, follower))) 
          print(f'You have start following {follower}') 
    
    def get_following_list(self, name):
        return self.__follow_map.get_connected_node(name)
    
    def get_follower_list(self, name, type_of:Literal['set', 'str']='set'):
        if type_of == 'set':
            return self.__follow_map.get_connected_to_node(name)
        elif type_of == 'str':
            return ', '.join(list(self.__follow_map.get_connected_to_node(name)))

@dataclass()
class User:
    def __post_init__(self):
        tweets: List[Tweets] = field(default_factory=list)
        
        
    def show_tweets(self):
        if len(self.tweets) == 0:
            print('You have no tweets to show, please add some tweets')
        else:
            return '\n'.join(self.tweets)
    




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
        

class Twitter:
    def __init__(self) -> None:
        self.__current_user = None
        self.__user_obj = None
    
    @property
    def current_user(self):
        return self.__current_user
    
    @property
    def user_obj(self):
        return self.__user_obj
    
    @user_obj.setter
    def set_user_obj(self, user:User):
        self.__user_obj = user
    
    def login(self, username:str):
        self.__current_user = username
        
    def logout(self):
        self.__current_user = None




def postTweet(userID, tweetBody):
    pass

def getNewFeed():
    pass

def follow():
    pass

def unfollow():
    pass
