import sqlite3
import psycopg2

class postgresql_converter():
    
    def __init__(self, db_name, Postgres_user, Postgres_pw):
        self.conn_sqlite = sqlite3.connect(db_name)
        self.cur_sqlite = self.conn_sqlite.cursor()
        
        self.conn_psql = psycopg2.connect(dbname=db_name[:-3], user=Postgres_user, host="/tmp/", password=Postgres_pw)
        self.cur_psql= self.conn_psql.cursor()
    
    def getTables_FromSQLite(self):
        self.cur_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.cur_sqlite.fetchall()
        # [('album',), ('artist',), ('customer',), ('employee',), ('genre',), ('invoice',), ('invoice_line',), ('media_type',), ('playlist',), ('playlist_track',), ('track',)]
    
    def getTableSchema(self, table_name):
        return self.conn_sqlite.execute("PRAGMA table_info({tn});".format(tn=table_name)).fetchall()
        # [(0, 'album_id', 'INTEGER', 1, None, 1), (1, 'title', 'NVARCHAR(160)', 1, None, 0), (2, 'artist_id', 'INTEGER', 1, None, 0)]
        
    def getData_FromSQLite(self, table_name):
        return self.conn_sqlite.execute("SELECT * FROM {tn};".format(tn=table_name)).fetchall()
    
    def create_postgresql_table(self, table_name, table_schema):
        
        # This look creates a lists of strings, one for each column to be added,
        # each string is carries the PRAGA data for that column and will
        # be used in the CREATE TABLE statement
        pragma = {}
        columns = []
        for column in table_schema:
        
            pragma['cid'] = column[0]
            pragma['name'] = column[1]
            pragma['notnull'] = column[3]
            pragma['dflt_value'] = column[4]
            
            if 'NVARCHAR' in column[2]:
                pragma['type'] = column[2].replace('NVARCHAR', 'VARCHAR')
            elif column[2] == 'DATETIME':
                pragma['type'] = 'TIMESTAMP'
            else:
                pragma['type'] = column[2]
                      
            if column[5] == 1 and table_name != 'playlist_track':
                pragma['pk'] = 'PRIMARY KEY'
            else:
                pragma['pk'] = ''
                
            columns.append('{cn} {ct} {pk}'.format(cn=pragma['name'], ct=pragma['type'], pk=pragma['pk']).strip())
            
        query = 'CREATE TABLE {tn} ('.format(tn=table_name) + ', '.join(columns) + ');'
        
        self.conn_psql.autocommit = True
        self.cur_psql.execute(query)
    
    def dumpData_IntoPostgreSQL(self, table, table_rows, table_schema):
         
        for row in table_rows:
            cleaned_row = self.clean_data_set(row, table_schema)
            self.cur_psql.execute("INSERT INTO %s VALUES %s" % (table, cleaned_row))
            
    def clean_data_set(self, tup, table_schema, bad_characters = ["'"]):
        cleaned_data = []

        for index, value in enumerate(tup):
            if type(value) is str:
                tmp = str(value)
                for c in bad_characters:
                    if c in value:
                        tmp = tmp.replace(c,"")
                cleaned_data.append(tmp)
            elif value is None and table_schema[index][2] != 'INTEGER':
                cleaned_data.append("")
            elif value is None and table_schema[index][2] == 'INTEGER':
                cleaned_data.append(0)
            else:
                cleaned_data.append(value)
        
        return tuple(cleaned_data)
    
    def convert(self):
        
        tables = self.getTables_FromSQLite()
        tables[:] = ['%s' % t for t in tables]
        for table_name in tables:
            print('Woring Table: {tn}\n'.format(tn=table_name))
            table_schema = self.getTableSchema(table_name)
            print(table_schema)
            table_rows = self.getData_FromSQLite(table_name)
            self.create_postgresql_table(table_name, table_schema)
            self.dumpData_IntoPostgreSQL(table_name, table_rows, table_schema)
            print('\nTable: {tn}\nData Loaded\n'.format(tn=table_name))
            
        self.conn_psql.commit()
            
            
        
        
    def close_all_connections(self):
        self.conn_sqlite.close()
        self.conn_psql.close()

DBconverter = postgresql_converter('chinook.db', 'kitestring', 'Chlorine35%')
DBconverter.convert()
DBconverter.close_all_connections()
