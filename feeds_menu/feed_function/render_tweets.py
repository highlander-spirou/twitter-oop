from __future__ import annotations
from helpers import pprint
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Twitter import TweetDatabase
    from data_structures.Stack import Node

def render_10_tweets(current_user:str, tweet_db:TweetDatabase, primer:Optional[Node]=None):
    """
    Render the following 10 tweets including start node
    """
    i = 0
    if current_user is not None:
        try:
            current_node = tweet_db.get_paginated_node(current_user, 0) if primer is None else primer.next_node
            while i < 10:
                id = current_node.data
                tweet = tweet_db.get_tweet_from_id(id)
                tweet_rendered_body = f'{tweet.timestamp} - {tweet.owner}: "{tweet.body}"'
                pprint(tweet_rendered_body)
                current_node = current_node.next_node
                i+=1
        except:
            print('You reached the end of your tweets')
            return
    return current_node


