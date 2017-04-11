from book.update import UpdateUseCase
from book.exceptions import BookNotFound, ValidationError
from book.exceptions import ValidationError
from unittest import mock
import pytest


@pytest.fixture
def usecase():
    repository = mock.Mock()
    update_usecase = UpdateUseCase(repository=repository)
    return update_usecase


def test_update_book(usecase):
    usecase.repository.update.return_value = mock.Mock()
    id = 'existbook'
    data = {
        'title': 'This is new title',
        'content': 'This is new content',
        'published_at': 1479888658
    }

    assert usecase.update(id=id, data=data ) is not None
    assert usecase.repository.update.call_count == 1


def test_update_book_not_found(usecase):
    id = 'nonexistbook'
    data = {
        'title': 'This is new title',
        'content': 'This is new content',
        'published_at': 1479888658
    }

    usecase.repository.get.return_value = None

    with pytest.raises(BookNotFound):
        usecase.update(id=id, data=data)
        usecase.repository.update.assert_not_called()


def test_update_invalid_data(usecase):
    id = 'existbook'
    data = {
        'title': '',
        'content': 'This is new content',
        'published_at': 1479888658
    }

    usecase.repository.update.return_value = None

    with pytest.raises(ValidationError):
        usecase.update(id=id, data=data)
    usecase.repository.update.assert_not_called()




