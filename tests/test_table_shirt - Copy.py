from lib import db_assert

table = "Shirt"


def test_rows_present():
    db_assert.assert_minimum_rows_present(table, 1)


def test_id_unique():
    db_assert.assert_unique(table, "Id")


def test_size_numeric():
    db_assert.assert_numeric(table, "Size")


def test_size_within_range():
    db_assert.assert_no_rows(
        "SELECT Id, Size FROM Shirt WHERE Size < 48 OR Size > 54")


def test_color_reference_valid():
    db_assert.assert_no_rows("""SELECT Shirt.Id FROM Shirt 
                      LEFT JOIN Color ON Shirt.Color_Id = Color.Id 
                      WHERE Shirt.Color_Id IS NULL""")
