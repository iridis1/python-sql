from lib import db_assert

hub_prefix = "H_"
sat_prefix = "S_"
foreign_key_postfix = "_Id"
timestamp_field = "Timestamp"
source_field = "Source"


def assert_hub_and_satellite_timestamps_valid(entity):
    sql = parse_sql(
        "SELECT * FROM {HubTable} h INNER JOIN {SatTable} s ON h.Id = s.{HubFk} WHERE s.Timestamp < h.Timestamp OR s.Timestamp IS NULL OR h.Timestamp IS NULL", entity)
    db_assert.assert_no_rows(sql)


def assert_hub_data_matches_source_data(entity, business_key_field):
    sql = parse_sql(
        "SELECT {BusKey} FROM {SrcTable} WHERE {BusKey} NOT IN (SELECT {BusKey} FROM {HubTable})", entity, business_key_field)
    db_assert.assert_no_rows(sql)


def assert_hub_source_valid(entity, source):
    sql = parse_sql(
        "SELECT {Source} FROM {HubTable} WHERE {Source} <> '%s'" % source, entity)
    db_assert.assert_no_rows(sql)


def assert_satellite_link_valid(entity):
    hub_key = entity + foreign_key_postfix
    sat_table = sat_prefix + entity
    db_assert.assert_unique_combination(sat_table, hub_key, timestamp_field)

    sql = parse_sql(
        "SELECT Id FROM {HubTable} WHERE Id NOT IN (SELECT {HubFk} FROM {SatTable})", entity)
    db_assert.assert_no_rows(sql)


def assert_satellite_source_valid(entity, source):
    sql = parse_sql(
        "SELECT {Source} FROM {SatTable} WHERE {Source} <> '%s'" % source, entity)
    db_assert.assert_no_rows(sql)


def assert_satellite_data_matches_source_data(entity, business_key_field, data_fields):
    sql = parse_sql("""SELECT * FROM {SrcTable} src
        INNER JOIN(
            SELECT hub.{BusKey}, %s FROM {HubTable} hub
            INNER JOIN (
                SELECT {HubFk}, %s, rownumber
                FROM (
                    SELECT
                        *,
                        ROW_NUMBER() OVER (PARTITION BY {HubFk} 
                        ORDER BY Timestamp DESC) AS rownumber
                        FROM {SatTable}) t
                WHERE t.rownumber = 1
            ) sat
            ON hub.id = sat.{HubFk}
        ) last_sat
        ON src.{BusKey}  = last_sat.{BusKey} 
        WHERE src.Name <> last_sat.Name""", entity, business_key_field) % (data_fields, data_fields)
    db_assert.assert_no_rows(sql)


def parse_sql(sql, entity, business_key_field="BusinessKeyNotProvided"):
    sql = sql.replace("{SrcTable}", entity)
    sql = sql.replace("{SatTable}", sat_prefix + entity)
    sql = sql.replace("{HubTable}", hub_prefix + entity)
    sql = sql.replace("{HubFk}", entity + foreign_key_postfix)
    sql = sql.replace("{BusKey}", business_key_field)
    sql = sql.replace("{Source}", source_field)
    return sql
