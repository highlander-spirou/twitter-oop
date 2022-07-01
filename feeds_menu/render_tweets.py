from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from RLinkedList import ReverseLinkedList

def render_tweets(tweets:ReverseLinkedList, n = 0):
    if n == 0:
        return tweets.traverse_to_n(n, 9)
    else:
        return tweets.traverse_to_n(n, n+9)
