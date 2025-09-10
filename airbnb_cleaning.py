
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\EzequielBochicchio\\OneDrive - THE NEXT PEAK S.L\\Escritorio\\Personal\\Python\\listings.csv")

# ver cantidad de columnas, de registros y tipos de datos
df.info()

# ver nulos en cada campo
df.isnull().sum()

# fila entera con duplicados
df.duplicated().sum()

print(df.columns.tolist())

# agrupación y conteo del campo "reviews_per_month"
df_reviews_per_month = df.groupby('reviews_per_month')["host_id"].count()
df_reviews_per_month

# agrupación y conteo del campo "last_reviews"
df_last_review = df.groupby('last_review')["host_id"].count().sort_values(ascending=False)
df_last_review

# Convierte el campo "last_reviews" en tipo datetime
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

# actualiza los null de los campos "name" y "host_name" a "Sin dato"
df['name'] = df['name'].fillna('Sin dato')
df['host_name'] = df['host_name'].fillna('Sin dato')

# actualiza los null del campo "reviews_per_month" a "Sin dato"
df['reviews_per_month'] = df['reviews_per_month'].fillna('Sin dato')

# actualiza los null del campo "license" a "Sin dato"
df['license'] = df['license'].fillna('Sin dato')

# analiza el campo "price"
df["price"].describe()

# distribución del campo "price"
sns.histplot(x="price", data = df, bins=50)

# agrupa el campo "price" y cuenta los que son mayores a 258
df_price = df.groupby('price')["host_id"].count()
df_price_filtrado = df_price[df_price.index > 258].sort_index(ascending=False)
df_price_filtrado

# outliers
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['price'] < Q1 - 1.5 * IQR) | (df['price'] > Q3 + 1.5 * IQR)]
outliers

outlier_price = df[df['price'] > 258]
outlier_price

# Agrupa y cuenta cuantos registros tienen un precio entre 71577 y 258
df_price = df.groupby('price')["host_id"].count()
df_price_filtrado = df_price[(df_price.index <= 71577) & (df_price.index >= 258)].sort_index(ascending=False)
df_price_filtrado

# Paso 1: Reemplazar los precios 0 por NaN
df['price'] = df['price'].replace(0, pd.NA)

# Paso 2: Calcular la mediana por barrio
medianas_barrio = df.groupby('neighbourhood_group')['price'].transform('median')

# Paso 3: Imputar los valores faltantes de 'price' con la mediana del barrio
df['price'] = df['price'].fillna(medianas_barrio)

df["price"].describe()

# Etiquetar los outliers para análisis separados
df['is_price_outlier'] = df['price'] > 258

# Crear un nuevo DataFrame con outliers de precio
df_outliers = df[df['price'] > 258].copy()
df_outliers

# setea como indice el campo "id"
df.set_index("id", inplace = True)

# conteo duplicados de host_id
df['host_id'].duplicated().sum()

# host_id duplicados
df[df['host_id'].duplicated()]['host_id'].unique()

# cuantos registros tiene cada host_id
df['host_id'].value_counts()

# conteo únicos de host_id
df['host_id'].nunique()

# extrae el año, el mes, el día y el nombre del día de la fecha de review
df['año'] = df['last_review'].dt.year
df['mes'] = df['last_review'].dt.month
df['día'] = df['last_review'].dt.day
df['día_semana'] = df['last_review'].dt.day_name()

# rellena con 0 los nulos
df['año'] = df['año'].fillna('0')

# cambia el tipo de dato a int64
df['año'] = df['año'].astype('int64')

# rellena con 0 los nulos y cambia el tipo de dato a int64
df['mes'] = df['mes'].fillna('0')
df['mes'] = df['mes'].astype('int64')
df['día'] = df['día'].fillna('0')
df['día'] = df['día'].astype('int64')

# Guardar el DataFrame como archivo Excel en la ruta especificada
df.to_excel(r"C:\\Users\\EzequielBochicchio\\OneDrive - THE NEXT PEAK S.L\\Escritorio\\Personal\\Python\\Airbnb_Madrid.xlsx", index=True)

print("Archivo exportado correctamente a Excel.")
