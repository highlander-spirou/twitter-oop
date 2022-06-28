from getpass import getpass


def login_prompt(self):
    username = input('Please enter your username: ')
    password = getpass(prompt='Please enter your password: ')
    user = self.get_db.query_user(username, password)
    if user is None:
        print('Username or password is invalid, please try again')
    else:
        self.get_app.login(username)
        self.sign_in_menu()
