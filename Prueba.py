import pymongo
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a la base de datos MongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client["Inventorio"]
collection = db["venta"]
# Consulta a la base de datos y obtención de los datos
data = list(collection.find())
df = pd.DataFrame(data)
# Seleccionar las columnas que deseas mostrar
columnas_a_mostrar = ['producto', 'cantidad', 'precio_unitario']
# Creación de un DataFrame de Pandas con los datos
df_mostrado = df[columnas_a_mostrar]
print(df_mostrado)
print("Medidas de Tendencia Central")

# Calcular medidas de tendencia central
media = df_mostrado['replacement_cost'].mean()
mediana = df_mostrado['replacement_cost'].median()
moda = df_mostrado['replacement_cost'].mode()[0]

# Imprimir las medidas de tendencia central
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
# Análisis de los datos (por ejemplo, agrupación por categoría y cálculo de sumas)
#grouped_data = df.groupby('categoria')['monto'].sum()

# Visualización de los datos (por ejemplo, un gráfico de barras)
#grouped_data.plot(kind='bar')
#plt.title('Ventas por Categoría')
#plt.xlabel('Categoría')
#plt.ylabel('Monto')
#plt.show()
