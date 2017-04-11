import jsonschema
from book import Book
from book.exceptions import ValidationError


class StoreUseCase(object):

    def __init__(self, repository):
        self.repository = repository

    def store(self, data):
        """
        Store a new book
        Args:
            data (dict): Dictionary of the new book
        Returns:
            src.book.Book
        Raises:
            ValidationError
        """
        try:
            jsonschema.validate(data, validation_schema, format_checker=jsonschema.FormatChecker())
        except jsonschema.ValidationError as e:
            raise ValidationError(e.message)

        book = Book(
            book_id=None,
            title=data["title"],
            content=data["content"],
            published_at=data["published_at"]
        )

        return self.repository.store(book)


validation_schema = {
    "type": "object",
    "$schema": "http://json-schema.org/draft-03/schema",
    "properties": {
        "title": {
            "type": "string",
            "required": True,
            "minLength": 1
        },
        "content": {
            "type": "string",
            "required": True,
            "minLength": 1
        },
        "published_at": {
            "type": "integer",
            "required": True
        },
    },
}
