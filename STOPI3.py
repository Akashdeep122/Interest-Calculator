import sqlite3
conn=sqlite3.connect("warnings.db")
cur=conn.cursor()
cur.execute("CREATE TABLE warns (name STRING, amount INTEGER, interest REAL, final REAL)")
conn.commit()
conn.close()
