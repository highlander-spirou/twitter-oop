from Twitter import Twitter, LoginDb, FollowMap, TweetList
from menu_functions import Menu

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
    Quit = input('Welcome to Twitter 🐦 \n Press Enter to continue \n Press Q to Quit')
    while Quit != "q" and IS_CONTINUE:
        state = run_program()
        IS_CONTINUE = state