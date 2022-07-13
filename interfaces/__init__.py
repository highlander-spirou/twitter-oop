from __future__ import annotations
from typing import TYPE_CHECKING, Optional, TypedDict
if TYPE_CHECKING:
    from Twitter import TweetDatabase, FollowMap
    from data_structures.Stack import Node
    

class ObserverInterface(TypedDict):
    current_user:str
    tweet_db:TweetDatabase
    follow_map:FollowMap
    initial_primer:Optional[Node]
    initial_followed_tweets_head: dict