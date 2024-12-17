from lib import db_assert

table = "Color"


def test_multiple_records_present():
    db_assert.assert_minimum_records_present(table, 3)


def test_id_unique():
    db_assert.assert_unique(table, "Id")


def test_name_not_empty():
    db_assert.assert_not_null(table, "Name")


def test_name_unique():
    db_assert.assert_unique(table, "Name")
