from book import Book


def test_book_attributes():
    book = Book(
        book_id='1234',
        title='This is title',
        content='This is content',
        published_at=1479885808
    )

    assert book.book_id == '1234'
    assert book.title == 'This is title'
    assert book.content == 'This is content'
    assert book.published_at == 1479885808


def test_book_to_dict():
    expected_book_dict = {
        'book_id': '1234',
        'title': 'This is title',
        'content': 'This is content',
        'published_at': 1479885808
    }
    book = Book(
        book_id='1234',
        title='This is title',
        content='This is content',
        published_at=1479885808
    )

    assert expected_book_dict == book.to_dict()