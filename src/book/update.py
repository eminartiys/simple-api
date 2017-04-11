import jsonschema
from book.exceptions import ValidationError
from book.exceptions import BookNotFound

class UpdateUseCase(object):

    def __init__(self, repository):
        self.repository = repository

    def update(self, id, data):
        """
        Update book
        Args:
            id , data (src.book.Book)
        Returns:
           (src.book.Book)
        """
        book = self.repository.get(id)

        if book is None:
            raise BookNotFound

        try:
            jsonschema.validate(data, validation_schema, format_checker=jsonschema.FormatChecker())
        except jsonschema.ValidationError as e:
            raise ValidationError(e.message)

        book.title = data["title"]
        book.content = data["content"]
        book.published_at = data["published_at"]

        return self.repository.update(book)


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