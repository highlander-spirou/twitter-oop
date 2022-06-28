from sign_in_classes.landing import landing
from helpers import add_functions_as_methods


@add_functions_as_methods((landing))
class SomeClass:
    def __init__(self, num) -> None:
        self.__app = num

    @property
    def get_app(self):
        return self.__app

    def pp(self):
        return self.__app


if __name__ == '__main__':
    a = SomeClass(3)
    print(a.pp())
    print(a.landing(4))