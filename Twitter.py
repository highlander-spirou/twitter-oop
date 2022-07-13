from datetime import datetime
from getpass import getpass
from dataclasses import dataclass, field
from typing import Dict, Literal, List, Tuple, TypedDict, Optional, Union
from helpers import create_random, extract_dict_keys, read_attribute
from data_structures.Graph import Graph, Edge
from data_structures.Stack import Stack, Node
from helpers import create_random

class Tweet:
    def __init__(self, tweet_body, tweet_owner, timestamp:datetime) -> None:
        self.__tweet_id = create_random()
        self.__tweet_body = tweet_body
        self.__tweet_owner = tweet_owner
        self.__create_at = timestamp

    @property
    def id(self):
        return self.__tweet_id

    @property
    def body(self):
        return self.__tweet_body

    @property
    def owner(self):
        return self.__tweet_owner

    @property
    def timestamp(self):
        return self.__create_at


@dataclass
class TweetIndexById:
    __tweets:Dict[str, Tweet] = field(default_factory=dict)

    def add_tweet(self, id, tweet:Tweet):
        self.__tweets[id] = tweet

    def get_tweet(self, id:str):
        return self.__tweets.get(id)

@dataclass
class TweetIndexByOwner:
    __tweets:Dict[str, Stack] = field(default_factory=dict)

    def add_to_user(self, username, tweet_id:str):
        if username in self.__tweets:
            self.__tweets[username].add(tweet_id)
        else:
            self.__tweets[username] = Stack()
            self.__tweets[username].add(tweet_id)

    def get_user_stack(self, username):
        return self.__tweets.get(username)
        
    pass

class TweetDatabase:
    def __init__(self) -> None:
        self.__owner_indices = TweetIndexByOwner()
        self.__id_indices = TweetIndexById()

    def create_tweet(self, username, body, timestamp):
        new_tweet = Tweet(body, username, timestamp)
        self.__id_indices.add_tweet(new_tweet.id, new_tweet)
        self.__owner_indices.add_to_user(username, new_tweet.id)


    def get_paginated_node(self, username, start):
        """
        Wrapper function to access get_nth_node() method of __owner_indices
        """
        user_stack = self.__owner_indices.get_user_stack(username)
        return user_stack.get_nth_node(start)

    def get_tweet_from_id(self, id:str):
        return self.__id_indices.get_tweet(id)

    def get_tweet_from_user(self, username:str):
        return self.__owner_indices.get_user_stack(username)

    




class FollowMap:
    def __init__(self) -> None:
        self.__follow_map = Graph()
        
    def add_follow(self, followee, follower):
          self.__follow_map.add_edge(Edge((followee, follower)))
          print(f'{followee} start following {follower}')
    
    def get_following_list(self, name):
        """
        Get the set of users that you started following
        """
        return self.__follow_map.get_connected_node(name)
    
    def get_follower_list(self, name, type_of:Literal['set', 'str']='set'):
        """
        Get the set of the user following you
        """
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
        self.__users:Dict[tuple, User] = {}
    
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


if __name__ == '__main__':
    tweet1 = Tweet('from nhan', 'nhan')
    tn = TweetNode({datetime(2022, 10, 22): tweet1})
    print(tn.get_timestamp_id())