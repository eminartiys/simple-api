from book.exceptions import BookNotFound


class GetUseCase(object):

    def __init__(self, repository):
        self.repository = repository

    def get(self, find_id):
        """
        Get a book by book_id
        Args:
           find_id (str)
        Returns:
           src.book.Book
        Raises:
            ValidationError
        """
        book = self.repository.get(find_id)

        if book is None:
            raise BookNotFound

        return book
