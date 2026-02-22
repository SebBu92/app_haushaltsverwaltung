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

def test_save_storage_without_value():
    mock_db = Mock()
    
    controller = StorageController(mock_db)

    with pytest.raises(ValueError):
        controller.save_storage("")

    mock_db.insert_storage.assert_not_called()

def test_save_storage_with_default_value():
    mock_db = Mock()

    controller = StorageController(mock_db)

    with pytest.raises(ValueError):
        controller.save_storage("Lagerort hinzufügen")

    mock_db.insert_storage.assert_not_called()

def test_save_storage_with_valid_value():
    pass

def test_delete_storage_without_value():
    mock_db = Mock()

    controller = StorageController(mock_db)

    with pytest.raises(ValueError):
        controller.delete_storage("")
    mock_db.insert_storage.assert_not_called()

def test_delete_storage_with_valid_value():
    pass
