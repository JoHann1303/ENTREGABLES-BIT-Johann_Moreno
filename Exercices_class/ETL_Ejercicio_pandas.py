import pandas as pd
df = pd.read_csv("Data_Bases/df_ventas.csv")
df.dataframe = df

#print(df.head(10))
print(df.isnull().sum())

print(df.duplicated().sum())

df["ciudad"] = df["ciudad"].fillna("Desconocida")
print(df["ciudad"].head(26))

print(df.isnull().sum())
print(df[df["ciudad"].isnull()].head(26))

mediana_edad = df["edad_cliente"].median()

df["edad_cliente"] = df["edad_cliente"].fillna(mediana_edad)