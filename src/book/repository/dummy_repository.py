from book import Book


class Dummy_Repository(object):

    def store(self, book):
        """
        Store an book
        Args:
           book (src.book.Book)
        Returns:
           src.book.Book
        """
        pass

    def get(self, book_id):
        """
        Get an book by book_id
        Args:
           book_id (str)
        Returns:
           src.book.Book
        """
        book = Book(
            book_id='1234',
            title='this is title',
            content='this is content',
            published_at=1479885808
        )

        return book

    def delete(self, book):
        """
        Delete book from storage
        Args:
          book (src.book.Book)
        Returns:
          None
        """
        pass

    def update(self, book):
        """
        Update book
        Args:
            book (src.book.Book)
        Returns:
           (src.book.Book)
        """
        pass
