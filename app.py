from Twitter import Twitter, LoginDb
from menu_functions import Menu
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from helpers import create_random

app = Twitter()
login_db = LoginDb()
menu = Menu(app, login_db)
IS_CONTINUE = True

def run_program():
    while True:
        global login_db
        if app.login_state is False:
            option_selection = input(OPTION_MENU['welcome'])
            try:
                if int(option_selection) in SELECTION_OPTIONS['welcome']:
                    if int(option_selection) == 1:
                        menu.sign_up_menu()
                        break
                    if int(option_selection) == 2:
                        menu.sign_in_menu()
                    if int(option_selection) == 3:
                        global IS_CONTINUE
                        IS_CONTINUE = False
                        break
                else:
                    raise InvalidInput(option_selection)
            except InvalidInput as e:
                print(e.message)
            except ValueError:
                print('Please type a number between 1 and 3')
        else:
            menu.sign_in_menu()

if __name__ == '__main__':
    user1 = login_db.create_user('nhan', '1')
    Quit = input('Welcome to Twitter 🐦 \n Press Enter to continue \n Press Q to Quit')
    while Quit != "q" and IS_CONTINUE:
        run_program()