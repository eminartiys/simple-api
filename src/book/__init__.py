class Book(object):

    def __init__(self, book_id, title, content, published_at):
        self.book_id = book_id
        self.title = title
        self.content = content
        self.published_at = published_at

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'content': self.content,
            'published_at': self.published_at
        }