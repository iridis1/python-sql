from lib import db_assert

hub_prefix = "H_"
sat_prefix = "S_"
foreign_key_postfix = "_Id"
primary_key = "_Id"
timestamp = "Timestamp"


def assert_satellite_link_valid(entity_name):
    hub_key = entity_name + foreign_key_postfix
    hub_table = hub_prefix + entity_name
    sat_table = sat_prefix + entity_name
    db_assert.assert_unique_combination(sat_table, hub_key, timestamp)
    # To be completed


def assert_hub_contains_all_business_keys(entity_name, business_key_field):
    hub_table = hub_prefix + entity_name
    db_assert.assert_no_rows("SELECT %s FROM %s WHERE %s NOT IN (SELECT %s FROM %s)" % (
        business_key_field, entity_name, business_key_field, business_key_field, hub_table))


# def assert_hub_matches_source(entity_name):
#     hub_key = entity_name + foreign_key_postfix
#     hub_table = hub_prefix + entity_name
#     sat_table = sat_prefix + entity_name

#     db_assert.assert_no_rows("""SELECT * FROM " +  
#                       LEFT JOIN %s ON %s.%s = %s.%s
#                       WHERE %s.%s IS NULL OR %s.%s IS NULL""" % (
#         entity_name, hub_table, entity_name, primary_key, hub_table
#     ))
