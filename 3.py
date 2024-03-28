from sqlalchemy import create_engine
import pandas as pd

cnx = create_engine('mysql+pymysql://root@localhost:3306/sakila').connect()
codigo = 'select amount from pagos'
data = pd.read_sql(codigo, cnx)
lista = pd.DataFrame(data.head())

# Calcular medidas de tendencia central
media = lista.mean()
mediana = lista.median()
moda = lista.mode()

# Imprimir las medidas de tendencia central
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

