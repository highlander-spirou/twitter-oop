from datetime import datetime
from collections import OrderedDict
from getpass import getpass
from dataclasses import dataclass, field
from typing import Dict, Literal, Optional
from helpers import create_random
from Graph import Graph, Edge
from RLinkedList import ReverseLinkedList

class Tweet:
    def __init__(self, tweet_body, tweet_owner) -> None:
        self.__tweet_body = tweet_body
        self.__tweet_owner = tweet_owner
        self.__tweet_id = create_random()

    def __repr__(self) -> str:
        return f'{self.__tweet_id}: {self.__tweet_body}'

@dataclass      
class TweetList:
    __tweets:Dict[str, ReverseLinkedList] = field(default_factory=OrderedDict)

    def add_tweet(self, username, body, timestamp):
        new_tweet = Tweet(body, username)
        linked_list = self.__tweets.get(username)
        if linked_list is None:
            tweet_list = ReverseLinkedList()
            tweet_list.add({timestamp: new_tweet})
            self.__tweets[username] = tweet_list
        else:
            linked_list.add({timestamp: new_tweet})
        print(f'Tweet added by {username}')

    def get_tweets_by_name(self, name:str):
        return self.__tweets.get(name)
    
 
class FollowMap:
    def __init__(self) -> None:
        self.__follow_map = Graph()
        
    def add_follow(self, followee, follower):
          self.__follow_map.add_edge(Edge((followee, follower))) 
    
    def get_following_list(self, name):
        return self.__follow_map.get_connected_node(name)
    
    def get_follower_list(self, name, type_of:Literal['set', 'str']='set'):
        if type_of == 'set':
            return self.__follow_map.get_connected_to_node(name)
        elif type_of == 'str':
            return ', '.join(list(self.__follow_map.get_connected_to_node(name)))

    def unfollow_user(self, start, stop):
        re = self.__follow_map.remove_edge(start, stop)
        if re is not None:
            print(f'Unfollow {re}')
        else:
            print('Cannot unfollow this user, neither follow or the username is correct')

@dataclass()
class User:
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


