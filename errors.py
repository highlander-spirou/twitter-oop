class InvalidInput(Exception):
    def __init__(self, input) -> None:
        self.input = input
        self.message = f'{input} is not a valid input'
        super().__init__(self.message)