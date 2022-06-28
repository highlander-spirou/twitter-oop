from constants import OPTION_MENU, SELECTION_OPTIONS


def follower_menu(self, current_user):
    print("\nFollowing list: ", self.get_map.get_following_list(current_user))
    option_selection = input(OPTION_MENU['follower'])
    if int(option_selection) == 1:
        user = input('Please type the username to follow: ')
        if self.get_db.search_username(user) is True:
            self.get_map.add_follow(current_user, user)
            print(f'✔ Follow user {user}')
        else:
            print(f'User {user} does not exists, please try a valid username')
        follower_menu(self, current_user)
    elif int(option_selection) == 2:
        user = input('Please type the username to unfollow: ')
        self.get_map.unfollow_user(current_user, user)
        follower_menu(self, current_user)
    elif int(option_selection) == 3:
        follow_menu(self)

def followee_menu(self, current_user):
    print("Follower list")
    print(f'\nYour Follower list: {self.get_map.get_follower_list(current_user, "str")} \n')
    follow_menu(self)

def follow_menu(self):
    current_user = self.get_app.current_user
    option_selection = input(OPTION_MENU['follow'])
    if int(option_selection) == 1:
        follower_menu(self, current_user)
    elif int(option_selection) == 2:
        followee_menu(self, current_user)

