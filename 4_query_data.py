import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Consultamos los datos
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

conn.close()
