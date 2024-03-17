
class MyBaseException(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

class TaskNotFoundException(MyBaseException):
    pass

class PonyNotWorkingException(MyBaseException):
    pass

class CeleryNotWorkingException(MyBaseException):
    pass



