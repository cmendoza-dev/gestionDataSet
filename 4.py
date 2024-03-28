from sqlalchemy import create_engine
import pandas as pd

cnx = create_engine('mysql+pymysql://root@localhost:3306/sakila').connect()
codigo = 'select replacement_cost from film'
data = pd.read_sql(codigo, cnx)
lista = pd.DataFrame(data)

# Calcular medidas de tendencia central
media = lista['replacement_cost'].mean()
mediana = lista['replacement_cost'].median()
moda = lista['replacement_cost'].mode()[0]

# Imprimir las medidas de tendencia central
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)


