import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Actualizamos la edad de Luis
cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (26, "Luis"))

conn.commit()
print("Datos actualizados.")
conn.close()
