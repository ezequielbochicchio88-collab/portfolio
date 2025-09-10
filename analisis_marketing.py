# ====================================================
# Análisis y Limpieza del Dataset de Marketing
# Autor: Ezequiel Bochicchio
# Fecha: 2025
# ====================================================

import pandas as pd
from datetime import datetime

# -------------------------------
# 1. Cargar dataset original
# -------------------------------
file_path = r"marketing_campaign.csv"  # Ajustar a la ruta de tu archivo
df = pd.read_csv(file_path, sep=';')

# Copiar para limpieza
df_clean = df.copy()

# -------------------------------
# 2. Transformaciones básicas
# -------------------------------
# Convertir fecha de cliente
df_clean['Dt_Customer'] = pd.to_datetime(df_clean['Dt_Customer'], format="%Y-%m-%d")

# Calcular edad (aprox. en 2025)
df_clean['Age'] = 2025 - df_clean['Year_Birth']

# Rellenar valores nulos en Income con la mediana
df_clean['Income'].fillna(df_clean['Income'].median(), inplace=True)

# Normalizar Marital_Status
df_clean['Marital_Status'] = df_clean['Marital_Status'].replace({
    'Alone': 'Single',
    'Absurd': 'Single',
    'YOLO': 'Single',
    'Divorced': 'Separated',
    'Widow': 'Separated'
})

# Crear columna Children
df_clean['Children'] = df_clean['Kidhome'] + df_clean['Teenhome']

# -------------------------------
# 3. Métricas de gasto y compras
# -------------------------------
# Total gastado
gasto_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
              'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df_clean['TotalSpent'] = df_clean[gasto_cols].sum(axis=1)

# Total de compras
df_clean['TotalPurchases'] = df_clean[['NumDealsPurchases', 'NumWebPurchases',
                                       'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)

# Gasto medio por compra
df_clean['AvgSpentPerPurchase'] = df_clean['TotalSpent'] / df_clean['TotalPurchases']
df_clean['AvgSpentPerPurchase'].fillna(0, inplace=True)

# -------------------------------
# 4. Otras variables derivadas
# -------------------------------
# Rango de edad
bins = [18, 30, 45, 60, 75, 100]
labels = ['18-29', '30-44', '45-59', '60-74', '75+']
df_clean['AgeGroup'] = pd.cut(df_clean['Age'], bins=bins, labels=labels, right=False)

# Nivel de ingresos (terciles)
df_clean['IncomeLevel'] = pd.qcut(df_clean['Income'], q=3, labels=['Bajo', 'Medio', 'Alto'])

# Días como cliente (hasta 01/01/2025)
df_clean['Customer_Days'] = (datetime(2025, 1, 1) - df_clean['Dt_Customer']).dt.days

# Campañas aceptadas totales
campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
df_clean['TotalAcceptedCmp'] = df_clean[campaign_cols].sum(axis=1)

# -------------------------------
# 5. Guardar dataset limpio
# -------------------------------
df_clean.to_csv("marketing_campaign_limpio.csv", index=False)

print("✅ Limpieza completada. Dataset guardado en 'marketing_campaign_limpio.csv'")
