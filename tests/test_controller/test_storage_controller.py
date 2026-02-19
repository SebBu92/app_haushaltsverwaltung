import pytest
from unittest.mock import Mock
from controller.storage_controller import StorageController

def test_get_storage_calls_db():
    mock_db = Mock()
    mock_db.get_storage.return_value = [("Keller",)]

    controller = StorageController(mock_db)
    result = controller.get_storage()

    mock_db.get_storage.assert_called_once()
    assert result == [("Keller",)]
