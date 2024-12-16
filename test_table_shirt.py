import lib.db_assert as db_assert
from lib.db_connect import cursor

table = "Shirt"

def test_records_present():
    db_assert.assert_minimum_records_present(table, 1)

def test_id_is_unique():
    db_assert.assert_is_unique(table, "Id")

def test_size_within_range():
    db_assert.assert_no_rows("SELECT Id, Size FROM Shirt WHERE Size < 48 OR Size > 54")

def test_color_reference_is_valid():
    sql = """SELECT COUNT(*) AS Count FROM Shirt 
                      LEFT JOIN Color ON Shirt.Color_Id = Color.Id 
                      WHERE Shirt.Color_Id IS NULL"""
    cursor.execute(sql)
    row = cursor.fetchone()
    assert row["Count"] == 0

