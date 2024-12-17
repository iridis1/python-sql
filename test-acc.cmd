set db_environment=acc
python -m pytest tests --numprocesses 2 --verbose --html results/report.html --junit-xml results/junit.xml