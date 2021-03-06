class Repository(object):

    def store(self, book):
        """
        Store a book
        Args:
           book (src.book.Book)
        Returns:
           src.book.Book
        """
        raise NotImplementedError

    def get(self, book_id):
        """
        Get an book by book_id
        Args:
           book_id (str)
        Returns:
           src.book.Book
        """
        raise NotImplementedError

    def delete(self, book):
        """
        Delete book from storage
        Args:
          book (src.book.Book)
        Returns:
          None
        """
        raise NotImplementedError

    def update(self, id, book):
        """
        Update book
        Args:
            book (src.book.Book)
        Returns:
           (src.book.Book)
        """
        raise NotImplementedError
