from copy import copy
from helpers import pprint
from feeds_menu.feed_function.render_tweets import render_10_tweets
from interfaces import ObserverInterface



def user_wall_menu(observer_state:ObserverInterface):
    copied_state = copy(observer_state)
    pprint("Here's all the tweet that you have posted: ")
    new_primer = render_10_tweets(copied_state['current_user'].current_user, copied_state['tweet_db'], copied_state['initial_primer'])
    if new_primer is not None:
        copied_state['initial_primer'] = new_primer
        quit_observing = input('Press "n" to get more tweets, "q" to quit')
        if quit_observing == "q":
            print('quit')
        elif quit_observing == 'n':
            print('continue')
            user_wall_menu(copied_state)
        else:
            print('wrong input')
    else:
        return
