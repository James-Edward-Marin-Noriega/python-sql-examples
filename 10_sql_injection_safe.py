import sqlite3

# Prevención de SQL Injection
conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Input de usuario (simulado)
entrada_usuario = "Luis"

# Consulta segura con placeholders
cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (entrada_usuario,))
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conn.close()
