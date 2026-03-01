import pytest
from unittest.mock import Mock
from controller.supplies_controller import SuppliesController

def test_get_supplies_calls_db():
    mock_db = Mock()
    mock_db.get_supplies.return_value = "Keller"

    controller = SuppliesController(mock_db)
    result = controller.get_supplies()

    mock_db.get_supplies.assert_called_once()
    assert result == "Keller"

def test_sort_by_mhd_asc():
    mock_db = Mock()

    controller = SuppliesController(mock_db)
    controller.sort_by_mhd("Aufsteigend")

    mock_db.sort_mhd_asc.assert_called_once()
    mock_db.sort_mhd_desc.assert_not_called()
    mock_db.get_supplies.assert_not_called()


def test_sort_by_mhd_desc():
    mock_db = Mock()

    controller = SuppliesController(mock_db)
    controller.sort_by_mhd("Absteigend")

    mock_db.sort_mhd_asc.assert_not_called()
    mock_db.sort_mhd_desc.assert_called_once_with()
    mock_db.get_supplies.assert_not_called()

def test_sort_by_mhd_with_value():
    mock_db = Mock()

    controller = SuppliesController(mock_db)
    controller.sort_by_mhd("Keller")

    mock_db.sort_mhd_asc.assert_not_called()
    mock_db.sort_mhd_desc.assert_not_called()
    mock_db.get_supplies.assert_called_once()



