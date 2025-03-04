from lib import db_assert

table = "Color"


def test_multiple_rows_present():
    db_assert.assert_minimum_rows_present(table, 3)


def test_id_unique():
    db_assert.assert_unique(table, "Id")


def test_name_not_empty():
    db_assert.assert_not_null(table, "Name")


def test_name_unique():
    db_assert.assert_unique(table, "Name")


def test_code_not_empty():
    db_assert.assert_not_null(table, "Code")


def test_code_unique():
    db_assert.assert_unique(table, "Code")
