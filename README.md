Execute the following steps to run the database tests in the test environment.

1 - Create a tst.env file with the following content:

```
db_server=serverName.database.windows.net
db_database=databaseName
db_user=user
```
2 - Set environmental variable `db_password`.

3 - Run `pip install -r -requirements.txt` to install the required packages.

4 - Execute `test-tst.cmd`. This script will run the tests in parallel and generate a test report.

