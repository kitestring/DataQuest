# Start the PostgreSQL command line tool by typing psql.
# Using the -U flag allow me to login as postgres user
kkite@mint18 ~ $ psql -U postgres
# Output:
# Password for user postgres: 
# psql.bin (9.6.6)
# Type "help" for help.
# Cannot read termcap database;
# using dumb terminal settings.
# postgres=# 



# Create a database called bank_accounts
postgres=# Create DATABASE bank_accounts;
# Output:
# CREATE DATABASE



# List all available databases.
postgres=# \l
postgres=# \q




# Switching databases
kkite@mint18 ~ $ psql -U postgres -d bank_accounts
bank_accounts=# CREATE TABLE deposits(id integer PRIMARY KEY, name TEXT, amount float);



# Creating Users
bank_accounts=# CREATE ROLE sec WITH CREATEDB LOGIN PASSWORD 'test';
bank_accounts=# \du




# Adding permissions
bank_accounts=# GRANT ALL PRIVILEGES ON deposits TO sec;
bank_accounts=# \dp deposits




# Removing permissions
bank_accounts=# REVOKE ALL PRIVILEGES ON deposits FROM sec;
bank_accounts=# \dp





# Superusers
bank_accounts=# CREATE ROLE aig WITH SUPERUSER LOGIN PASSWORD 'test';
bank_accounts=# \du
bank_accounts=# \q
kkite@mint18 ~ $ 