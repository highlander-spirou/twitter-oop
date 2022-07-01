from Twitter import Twitter, LoginDb, FollowMap, TweetList
from menu_functions import Menu
from datetime import datetime

IS_CONTINUE = True

app = Twitter()
login_db = LoginDb()
follow_graph = FollowMap()
tweet_list = TweetList()
menu = Menu(app, login_db, follow_graph, tweet_list)


def run_program():
    while True:
        return menu.menu_landing()
        

if __name__ == '__main__':
    user1 = login_db.create_user('nhan', '1')
    user2 = login_db.create_user('nhu', '1')
    user2 = login_db.create_user('map', '1')
    tweet1 = tweet_list.add_tweet('nhan', 'haha1', datetime(2022, 7, 1, 18, 26, 20))
    tweet2 = tweet_list.add_tweet('nhan', 'haha2', datetime(2022, 7, 1, 18, 26, 59))
    tweet4 = tweet_list.add_tweet('nhan', 'haha3', datetime(2022, 7, 1, 18, 30, 0))
    tweet5 = tweet_list.add_tweet('nhan', 'haha4', datetime(2022, 7, 1, 18, 30, 0))
    tweet6 = tweet_list.add_tweet('nhan', 'haha5', datetime(2022, 7, 1, 18, 31, 0))
    tweet7 = tweet_list.add_tweet('nhan', 'haha6', datetime(2022, 7, 1, 18, 33, 0))
    tweet8 = tweet_list.add_tweet('nhan', 'haha7', datetime(2022, 7, 1, 18, 35, 0))
    tweet9 = tweet_list.add_tweet('nhan', 'haha8', datetime(2022, 7, 1, 18, 40, 0))
    tweet10 = tweet_list.add_tweet('nhan', 'haha9', datetime(2022, 7, 1, 19, 0, 0))
    tweet11 = tweet_list.add_tweet('nhan', 'haha10', datetime(2022, 7, 1, 19, 10, 0))
    tweet12 = tweet_list.add_tweet('nhan', 'haha11', datetime(2022, 7, 1, 19, 20, 0))
    tweet13 = tweet_list.add_tweet('nhan', 'haha12', datetime(2022, 7, 1, 19, 30, 0))
    tweet14 = tweet_list.add_tweet('nhan', 'haha13', datetime(2022, 7, 1, 19, 40, 0))
    tweet15 = tweet_list.add_tweet('nhan', 'haha14', datetime(2022, 7, 1, 19, 50, 0))
    
    Quit = input('Welcome to Twitter 🐦 \n Press Enter to continue \n Press Q to Quit')
    while Quit != "q" and IS_CONTINUE:
        state = run_program()
        IS_CONTINUE = state