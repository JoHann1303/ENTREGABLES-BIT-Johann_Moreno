import pandas as pd 
import numpy as np

clientes = pd.read_excel("Data_Bases/Clientes.xlsx")
ventas = pd.read_excel("Data_Bases/Ventastaller.xlsx")


# print(clientes.head())
# print(ventas.head(3))
#s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# print(s)
#print(clientes.tail())
print(f"Muestra las 10 primeras filas del DataFrame ventas")

print( ventas.head(10))
print("////////////////////////////////////////////////////////////////////////////////////////////")

print(f"Número de filas en el DataFrame ventas: {len(ventas)} ")
print("Datos de las colunas producto y Precio_Unitario del DataFrame ventas")
ventas_Taller = ventas[["Producto", "Precio_Unitario"]]
print(ventas_Taller)
print("////////////////////////////////////////////////////////////////////////////////////////////")
Productos_Mayores_100 = ventas[ventas["Precio_Unitario"] > 100000]
print(Productos_Mayores_100[["Producto", "Precio_Unitario"]])
print("////////////////////////////////////////////////////////////////////////////////////////////")
Precio_Final = ventas.copy()
Precio_Final["Precio_Final"] = ventas["Precio_Unitario"] * ventas["Cantidad"]
print(Precio_Final[["Producto", "Precio_Unitario", "Cantidad", "Precio_Final"]])
print("////////////////////////////////////////////////////////////////////////////////////////////")
laptops_unicas = Precio_Final[Precio_Final["Producto"] == "Laptop"]["Producto"]
print(laptops_unicas)
