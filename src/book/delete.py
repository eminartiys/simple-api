from book.exceptions import BookNotFound


class DeleteUseCase(object):

    def __init__(self, repository):
        self.repository = repository

    def delete(self, id):
        """
        Delete a book by book_id
        Args:
           id (str)
        Returns:
           None
        Raises:
            BookNotFound
        """
        book = self.repository.get(id)

        if book is None:
            raise BookNotFound

        self.repository.delete(id)
