from lib.db_connect import cursor


def assert_minimum_records_present(table_name, minimum=1):
    sql = "SELECT COUNT(*) AS Count FROM %s" % table_name
    print(sql)
    cursor.execute(sql)
    count = cursor.fetchone()["Count"]
    assert count >= minimum


def assert_not_null(table_name, field_name):
    assert_no_rows("SELECT %s FROM %s WHERE %s IS NULL OR %s = ''" % (
        field_name, table_name, field_name, field_name))


def assert_unique(table_name, field_name):
    assert_no_rows("SELECT %s FROM %s GROUP BY %s HAVING COUNT(%s) > 1" % (
        field_name, table_name, field_name, field_name))


def assert_no_rows(sql):
    print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print(rows)
    assert len(rows) == 0
