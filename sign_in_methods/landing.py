from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput

def landing_page(self):
    if self.get_app.current_user is None:
        option_selection = input(OPTION_MENU['welcome'])
        try:
            if int(option_selection) in SELECTION_OPTIONS['welcome']:
                if int(option_selection) == 1:
                    self.sign_up_menu()
                if int(option_selection) == 2:
                    self.sign_in_menu()
                if int(option_selection) == 3:
                    return False
            else:
                raise InvalidInput(option_selection)
        except InvalidInput as e:
            print(e.message)
        except ValueError:
            print('Please type a number between 1 and 3')
    else:
        self.sign_in_menu()