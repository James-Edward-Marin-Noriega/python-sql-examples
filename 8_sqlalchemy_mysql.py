from sqlalchemy import create_engine
import pandas as pd

# Cambia user, password, host y dbname por tus datos
engine = create_engine("mysql+mysqlconnector://user:password@localhost/dbname")

# Lee una tabla de MySQL
df = pd.read_sql("SELECT * FROM usuarios", engine)
print(df)
