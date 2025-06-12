import sqlite3
import pandas as pd

conn = sqlite3.connect("ejemplo.db")

# Leemos una tabla SQL como DataFrame
df = pd.read_sql_query("SELECT * FROM usuarios", conn)
print(df)

conn.close()
