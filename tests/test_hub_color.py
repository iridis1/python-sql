from lib import db_assert
from lib import db_assert_data_vault

entity = "Color"
table = "H_" + entity
business_key_field = "Code"


def test_multiple_rows_present():
    db_assert.assert_minimum_rows_present(table, 3)


def test_id_unique():
    db_assert.assert_unique(table, "Id")


def test_business_key_not_empty():
    db_assert.assert_not_null(table, business_key_field)


def test_business_key_unique():
    db_assert.assert_unique(table, business_key_field)


def test_hub_contains_all_business_keys():
    db_assert_data_vault.assert_hub_data_matches_source_data(
        entity, business_key_field)


def test_hub_source_valid():
    db_assert_data_vault.assert_hub_source_valid(entity, "SAP")
