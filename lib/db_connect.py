from os import getenv
from dotenv import load_dotenv
import pymssql

db_environment = getenv("db_environment")

if db_environment == "":  # Use test environment as default.
    db_environment = "tst"

try:
    load_dotenv(f"{db_environment}.env")
except FileNotFoundError:
    print("Error: No .env file found.")

conn = pymssql.connect(
    server=getenv("db_server"),
    user=getenv("db_user"),
    password=getenv("db_password"),
    database=getenv("db_database"),
    as_dict=True)

cursor = conn.cursor()
