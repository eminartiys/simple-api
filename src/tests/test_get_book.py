from book.get import GetUseCase
from book.exceptions import BookNotFound
from unittest import mock
import pytest


@pytest.fixture
def usecase():
    repository = mock.Mock()
    get_usecase = GetUseCase(repository=repository)
    return get_usecase


def test_get_book(usecase):
    find_id = 'existbook'
    usecase.repository.get.return_value = mock.Mock()

    assert usecase.get(find_id=find_id) is not None
    assert usecase.repository.get.call_count == 1


def test_get_book_not_found(usecase):
    find_id = 'nonexistsbook'
    usecase.repository.get.return_value = None

    with pytest.raises(BookNotFound):
        usecase.get(find_id=find_id)
    assert usecase.repository.get.call_count == 1