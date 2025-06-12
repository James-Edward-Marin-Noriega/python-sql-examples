import psycopg2

# Conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mi_basedatos",
    user="mi_usuario",
    password="mi_clave"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")
print("Versión de PostgreSQL:", cursor.fetchone())

conn.close()
