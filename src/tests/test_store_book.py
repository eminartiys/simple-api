from book.exceptions import ValidationError
from book.store import StoreUseCase
from unittest import mock
import pytest


@pytest.fixture()
def usecase():
    repository = mock.Mock()
    store_usecase = StoreUseCase(repository=repository)

    return store_usecase


def test_store_usecase(usecase):
    data = {
        'title': 'This is title',
        'content': 'This is content',
        'published_at': 1479888658
    }
    usecase.repository.store.return_value = mock.Mock()

    assert usecase.store(data) is not None
    assert usecase.repository.store.call_count == 1


def test_store_invalid_data(usecase):
    data = {
        'title': '',
        'content': 'this is content',
        'published_at': 1479888658
    }
    usecase.repository.store.return_value = None

    with pytest.raises(ValidationError):
        usecase.store(data)
    usecase.repository.store.assert_not_called()

