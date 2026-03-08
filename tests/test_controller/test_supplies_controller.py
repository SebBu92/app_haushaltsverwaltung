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

def test_delete_supplies_without_value():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.delete_supplies(-1)

    mock_db.delete_supplies.assert_not_called()

def test_delete_supplies_with_valid_value():
    mock_db = Mock()
    mock_db.delete_supplies.return_value = None

    controller = SuppliesController(mock_db)
    result = controller.delete_supplies(1)

    mock_db.delete_supplies.assert_called_once_with(1)
    assert result is None

def test_add_quantity_with_invalid_id():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(5, -1)

    mock_db.add_quantity.assert_not_called()

def test_add_quantity_with_quantity_smaller_one():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(0, 1)

    mock_db.add_quantity.assert_not_called()

def test_add_quantity_with_quantity_bigger_hundred():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(101, 1)

    mock_db.add_quantity.assert_not_called()

def test_add_quantity_with_valid_value():
    mock_db = Mock()
    mock_db.add_quantity.return_value = 5

    controller = SuppliesController(mock_db)
    result = controller.add_quantity(100, 1)

    mock_db.add_quantity.assert_called_once_with(100, 1)
    assert result == 5

def test_sub_quantity_with_invalid_id():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(5, -1)

    mock_db.add_quantity.assert_not_called()

def test_sub_quantity_with_quantity_smaller_one():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(0, 1)

    mock_db.add_quantity.assert_not_called()

def test_sub_quantity_with_quantity_bigger_hundred():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.add_quantity(101, 1)

    mock_db.add_quantity.assert_not_called()

def test_sub_quantity_with_valid_value():
    mock_db = Mock()
    mock_db.add_quantity.return_value = 5

    controller = SuppliesController(mock_db)
    result = controller.add_quantity(100, 1)

    mock_db.add_quantity.assert_called_once_with(100, 1)
    assert result == 5

def test_update_storage_without_value():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_storage("", 1)

    mock_db.update_strorage.assert_not_called()

def test_update_storage_with_valid_value():
    mock_db = Mock()
    mock_db.update_storage.return_value = "Abstellraum"

    controller = SuppliesController(mock_db)
    result = controller.update_storage("Abstellraum", 3)

    mock_db.update_storage.assert_called_once_with("Abstellraum", 3)
    assert result == "Abstellraum"

def test_update_mhd_with_dot_front():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2021.07-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_dot_back():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2021-07.01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_invalid_length():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2021-407-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_invalid_format():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("20210-7-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_invalid_year():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2019-07-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_month_smaller_one():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2022-00-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_month_bigger_12():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2022-13-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_day_smaller_one():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2022-00-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_day_bigger_31():
    mock_db = Mock()
    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.update_mhd("2022-32-01", 1)

    mock_db.update_mhd.assert_not_called()

def test_update_mhd_with_valid_value():
    mock_db = Mock()
    mock_db.update_mhd.return_value = "2025-12-12"

    controller = SuppliesController(mock_db)
    result = controller.update_mhd("2025-12-12", 3)

    mock_db.update_mhd.assert_called_once_with("2025-12-12", 3)
    assert result == "2025-12-12"

def test_save_supplies_invalid_type_quantity():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "Keller", "2025-12-12", "F")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_quantity_smaller_null():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "Keller", "2025-12-12", "-1")

    mock_db.insert_supplies.assert_not_called()




def test_save_supplies_quantity_bigger_hundred():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "Keller", "2025-12-12", "101")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_without_name():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("", "Keller", "2025-12-12", "1")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_default_name():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Bezeichnung Vorrat", "Keller", "2025-12-12", "2")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_without_storage():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "", "2025-12-12", "3")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_without_mhd():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "Keller", "", "4")

    mock_db.insert_supplies.assert_not_called()

def test_save_supplies_default_mhd():
    mock_db = Mock()

    controller = SuppliesController(mock_db)

    with pytest.raises(ValueError):
        controller.save_supplies("Kekse", "Keller", "MHD (JJJJ-MM-DD)", "5")

    mock_db.insert_supplies.assert_not_called()




def test_save_supplies_with_valid_values():
    mock_db = Mock()
    mock_db.insert_supplies.return_value = ("Pesto", "Kühlschrank", "2026-09-30", 13)

    controller = SuppliesController(mock_db)
    result = controller.save_supplies("Nutella", "Regal Links", "2027-05-30", "2")

    mock_db.insert_supplies.assert_called_once_with("Nutella", "2", "Regal Links", "2027-05-30")
    assert result == ("Pesto", "Kühlschrank", "2026-09-30", 13)






























