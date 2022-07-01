from __future__ import annotations
from constants import OPTION_MENU, SELECTION_OPTIONS
from errors import InvalidInput
from helpers import pprint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from menu_functions import Menu

def menu_landing(self:Menu):
    if self.get_app.current_user is None:
        option_selection = input(OPTION_MENU['welcome'])
        try:
            if int(option_selection) in SELECTION_OPTIONS['welcome']:
                if int(option_selection) == 1:
                    self.sign_up_menu()
                if int(option_selection) == 2:
                    self.user_menu()
                if int(option_selection) == 3:
                    return False
            else:
                raise InvalidInput(option_selection)
        except InvalidInput as e:
            print(e.message)
        except ValueError:
            pprint('Please type a number between 1 and 3')
    else:
        self.user_menu()