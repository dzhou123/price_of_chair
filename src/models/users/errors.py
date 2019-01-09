__author__ = 'dzhou'


class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass
