from Twitter import Twitter, LoginDb, FollowMap, TweetDatabase
from menu_functions import Menu
from test_add_tweet import create_tweets

IS_CONTINUE = True

app = Twitter()
login_db = LoginDb()
follow_graph = FollowMap()
tweet_list = TweetDatabase()
menu = Menu(app, login_db, follow_graph, tweet_list)


def run_program():
    while True:
        return menu.menu_landing()
        

if __name__ == '__main__':
    user1 = login_db.create_user('nhan', '1')
    user2 = login_db.create_user('nhu', '1')
    user2 = login_db.create_user('map', '1')
    follow_graph.add_follow('nhan', 'nhu')
    follow_graph.add_follow('nhan', 'map')

    create_tweets(tweet_list, 50)

    # dependent hook on login event
    app.login('nhan')
    follow_user_set = menu.get_map.get_following_list(menu.get_app.current_user)
    menu.state['initial_followed_tweets_head'] = {i: menu.get_tweets.get_tweet_from_user(i) for i in follow_user_set}

    Quit = input('Welcome to Twitter 🐦 \n Press Enter to continue \n Press Q to Quit')
    while Quit != "q" and IS_CONTINUE:
        state = run_program()
        IS_CONTINUE = state