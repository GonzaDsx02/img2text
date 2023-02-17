import duckdb
import os
from pathlib import Path
#metabase UID:GID = 2000:2000

con = duckdb.connect(database='db.duckdb', read_only=False)

# #con.execute("SHOW TABLES")
# print(con.execute("SHOW TABLES").fetchall())
def haveParquets(dir):
    for file in os.listdir("./"+folder):
            if file.endswith(".parquet"):
                return True

for folder in next(os.walk('.'))[1]:
    if(haveParquets(folder)):
        con.execute(f"CREATE TABLE '{folder}' AS SELECT * FROM './{folder}/*.parquet'")

con.close()
print("Success")