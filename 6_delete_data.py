import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Eliminamos un registro
cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Ana",))

conn.commit()
print("Datos eliminados.")
conn.close()

