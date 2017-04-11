from book.exceptions import BookNotFound
from book.delete import DeleteUseCase
from unittest import mock
import pytest


@pytest.fixture
def usecase():
    repository = mock.Mock()
    delete_usecase = DeleteUseCase(repository=repository)

    return delete_usecase


def test_delete_usecase(usecase):
    id = 'existbook'
    usecase.repository.get.return_value = mock.Mock()

    usecase.delete(id=id)
    assert usecase.repository.delete.call_count == 1


def test_delete_data_not_found(usecase):
    id = 'nonexistbook'
    usecase.repository.get.return_value = None

    with pytest.raises(BookNotFound):
        usecase.delete(id=id)
    usecase.repository.delete.assert_not_called()
