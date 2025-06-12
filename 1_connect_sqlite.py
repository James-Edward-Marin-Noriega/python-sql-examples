# Conexión básica a SQLite
import sqlite3

# Creamos o abrimos una base de datos local
conn = sqlite3.connect("ejemplo.db")

# Creamos un cursor para ejecutar comandos SQL
cursor = conn.cursor()

print("Conexión a SQLite exitosa.")
conn.close()
