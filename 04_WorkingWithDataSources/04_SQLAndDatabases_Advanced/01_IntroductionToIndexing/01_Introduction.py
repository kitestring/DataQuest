import sqlite3
conn = sqlite3.connect("factbook.db")

q = 'PRAGMA table_info(facts);'

schema = conn.execute(q).fetchall()

for s in schema:
    print(s)
    
# Returns:
#     (0, 'id', 'INTEGER', 1, None, 1)
#     (1, 'code', 'varchar(255)', 1, None, 0)
#     (2, 'name', 'varchar(255)', 1, None, 0)
#     (3, 'area', 'integer', 0, None, 0)
#     (4, 'area_land', 'integer', 0, None, 0)
#     (5, 'area_water', 'integer', 0, None, 0)
#     (6, 'population', 'integer', 0, None, 0)
#     (7, 'population_growth', 'float', 0, None, 0)
#     (8, 'birth_rate', 'float', 0, None, 0)
#     (9, 'death_rate', 'float', 0, None, 0)
#     (10, 'migration_rate', 'float', 0, None, 0)
#     (11, 'created_at', 'datetime', 0, None, 0)
#     (12, 'updated_at', 'datetime', 0, None, 0)