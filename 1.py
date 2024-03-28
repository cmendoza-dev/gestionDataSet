from sqlalchemy import create_engine
import pandas as pd

cnx = create_engine('mysql+pymysql://root@localhost:3306/sakila').connect()
codigo = 'select * from actor'
data = pd.read_sql(codigo, cnx)
lista = pd.DataFrame(data)
print(lista)
regs = len(lista.index)
cols = len(lista.count())
print("Registros: ", regs)
print("Campos; ", cols)
