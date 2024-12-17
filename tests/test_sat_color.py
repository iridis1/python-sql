from lib import db_assert
from lib import db_assert_data_vault

entity = "Color"
table = "S_" + entity


def test_multiple_rows_present():
    db_assert.assert_minimum_rows_present(table, 3)


def test_name_not_empty():
    db_assert.assert_not_null(table, "Name")


def test_name_unique():
    db_assert.assert_unique(table, "Name")


def test_assert_satellite_link_valid():
    db_assert_data_vault.assert_satellite_link_valid(entity)
