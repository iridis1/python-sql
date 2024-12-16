Execute the following steps to run the database tests:

1 - Create an .env file with the following content:

```
db_server=serverName.database.windows.net
db_database=databaseName
db_user=user
```
2 - Set environmental variable `db_password`.

3 - Run `pip install -r -requirements.txt`.

4 - Execute `test.cmd`.

