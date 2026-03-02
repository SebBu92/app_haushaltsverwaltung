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

def test_sort_by_mhd_without_value():
    mock_db = Mock()

    controller = SuppliesController(mock_db)
    controller.sort_by_mhd("Keller")

    mock_db.sort_mhd_asc.assert_not_called()
    mock_db.sort_mhd_desc.assert_not_called()
    mock_db.get_supplies.assert_called_once()

def test_filter_supplies_entry_without_value():
    mock_db = Mock()
    mock_db.get_supplies.return_value = ["Pesto", "Kekse"]

    controller = SuppliesController(mock_db)
    result = controller.filter_supplies_by_entry("")

    mock_db.get_supplies.assert_called_once_with()
    mock_db.sort_supplies.assert_not_called()
    assert result == ["Pesto", "Kekse"]

def test_filter_supplies_entry_with_value():
    mock_db = Mock()
    mock_db.sort_supplies.return_value = "Pesto"

    controller = SuppliesController(mock_db)
    result = controller.filter_supplies_by_entry("Pesto")

    mock_db.get_supplies.assert_not_called()
    mock_db.sort_supplies.assert_called_once_with("Pesto")
    assert result == "Pesto"

def test_filter_supplies_entry_with_wildcard():
    mock_db = Mock()
    mock_db.sort_supplies.return_value = "%Pesto%"

    controller = SuppliesController(mock_db)
    result = controller.filter_supplies_by_entry("*Pesto*")

    mock_db.get_supplies.assert_not_called()
    mock_db.sort_supplies.assert_called_once_with("%Pesto%")
    assert result == "%Pesto%"

def test_filter_supplies_entry_with_many_wildcards():
    mock_db = Mock()
    mock_db.sort_supplies.return_value = "%Pes%t%o%"

    controller = SuppliesController(mock_db)
    result = controller.filter_supplies_by_entry("*Pes*t*o*")

    mock_db.get_supplies.assert_not_called()
    mock_db.sort_supplies.assert_called_once_with("%Pes%t%o%")
    assert result == "%Pes%t%o%"


