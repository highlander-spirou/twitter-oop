from __future__ import annotations
from getpass import getpass
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from menu_functions import Menu


def login_prompt(self:Menu):
    username = input('Please enter your username: ')
    password = getpass(prompt='Please enter your password: ')
    user = self.get_db.query_user(username, password)
    if user is None:
        print('Username or password is invalid, please try again')
    else:
        self.get_app.login(username)
        self.user_menu()
