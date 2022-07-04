from datetime import datetime
from getpass import getpass
from dataclasses import dataclass, field
from typing import Dict, Literal, List, Tuple, TypedDict, Optional, Union
from helpers import create_random, extract_dict_keys, read_attribute
from Graph import Graph, Edge
from RLinkedList import ReverseLinkedList, Node

class Tweet:
    def __init__(self, tweet_body, tweet_owner) -> None:
        self.__tweet_body = tweet_body
        self.__tweet_owner = tweet_owner
        self.__tweet_id = create_random()

    @property
    def id(self):
        return self.__tweet_id

    @property
    def body(self):
        return self.__tweet_body


class TweetNodeInterface(TypedDict):
    timestamp: datetime
    tweet: Tweet

class TweetNode(Node):
    def __init__(self, data:TweetNodeInterface) -> None:
        super().__init__(data)

    def get_timestamp_id(self, attr:Literal['timestamp', 'id']='timestamp'):
        if attr == 'timestamp':
            return extract_dict_keys(self.data)
        elif attr == 'id':
            return read_attribute(self.data, 'id')


class TweetStack(ReverseLinkedList):
    def __init__(self) -> None:
        super().__init__()

    def add(self, data):
        new_node = TweetNode(data)
        old_head = None
        if self.is_empty():
            self.head = new_node
            self.count += 1
        else:
            old_head = self.head
            self.head = new_node
            self.head.next_node = old_head
            self.count += 1

@dataclass      
class TweetIndexByOwner:
    __tweets:Dict[str, TweetStack] = field(default_factory=dict)

    def add_tweet(self, username, timestamp, tweet:Tweet):
        existed_username = self.__tweets.get(username)
        if existed_username is None:
            tweet_stack = TweetStack()
            tweet_stack.add({timestamp: tweet})
            self.__tweets[username] = tweet_stack
        else:
            existed_username.add({timestamp: tweet})

    def get_tweets(self, name:str):
        if name in self.__tweets:
            return self.__tweets.get(name)
        return


@dataclass
class TweetIndexById:
    __tweets:Dict[str, Tweet] = field(default_factory=dict)

    def add_tweet(self, id, tweet:Tweet):
        self.__tweets[id] = tweet

    def get_tweet(self, id:str):
        if id in self.__tweets:
            return self.__tweets.get(id)
        return

class TweetList:
    def __init__(self) -> None:
        self.__owner_indices = TweetIndexByOwner()
        self.__id_indices = TweetIndexById()

    def create_tweet(self, username, body, timestamp):
        new_tweet = Tweet(body, username)
        self.__owner_indices.add_tweet(username, timestamp, new_tweet)
        self.__id_indices.add_tweet(new_tweet.id, new_tweet)

    def get_tweets_by_name(self, username):
        return self.__owner_indices.get_tweets(username)

    def get_head_tweet_by_name(self, username) -> Optional[TweetNode]:
        return self.__owner_indices.get_tweets(username).head

    def get_tweet_by_id(self, id):
        return self.__id_indices.get_tweet(id)


class FollowMap:
    def __init__(self) -> None:
        self.__follow_map = Graph()
        
    def add_follow(self, followee, follower):
          self.__follow_map.add_edge(Edge((followee, follower)))
          print(f'{followee} start following {follower}')
    
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


if __name__ == '__main__':
    tweet1 = Tweet('from nhan', 'nhan')
    tn = TweetNode({datetime(2022, 10, 22): tweet1})
    print(tn.get_timestamp_id())