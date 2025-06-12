import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Insertamos datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Ana", 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Luis", 25))

conn.commit()
print("Datos insertados.")
conn.close()
