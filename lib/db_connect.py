from os import getenv
from dotenv import load_dotenv
import pymssql

load_dotenv()

conn = pymssql.connect(
    server=getenv("db_server"),
    user=getenv("db_user"),
    password=getenv("db_password"),
    database=getenv("db_database"),
    as_dict=True)

cursor = conn.cursor()
