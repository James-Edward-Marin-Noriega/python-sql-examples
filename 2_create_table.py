import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Creamos una tabla simple
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

print("Tabla creada exitosamente.")
conn.commit()
conn.close()
