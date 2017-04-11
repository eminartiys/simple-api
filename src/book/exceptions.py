class Error(Exception):
    def __init__(self, message):
        self.message = message


class ValidationError(Error):
    pass


class BookNotFound(Error):
    def __init__(self):
        super(BookNotFound, self).__init__("Book Not Found")
