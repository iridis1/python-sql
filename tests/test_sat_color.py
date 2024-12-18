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


def test_satellite_source_valid():
    db_assert_data_vault.assert_satellite_source_valid(entity, "SAP")


def test_satellite_timestamp_valid():
    db_assert_data_vault.assert_hub_and_satellite_timestamps_valid(entity)


def test_satellite_data_matches_source_data():
    db_assert_data_vault.assert_satellite_data_matches_source_data(
        entity, "Code", "Name")
