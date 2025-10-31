# 🚀 Portfolio de Análisis de Datos

¡Hola! Soy Ezequiel, Profesional del Marketing con más de 10 años de trayectoria y experiencia en posiciones de análisis de datos e inteligencia de negocio.
Este portfolio reúne mis principales proyectos personales en análisis y visualización de datos.

---
## 📌 Proyectos

### 1. Dashboard de Marketing
**Descripción:**  
Reporte en Power BI que analiza datos de clientes y compras para entender patrones de consumo y comportamiento.  

**Objetivos:**  
- Identificar gasto total, número de compras y ticket medio.  
- Analizar la segmentación por edades, estado civil, cantidad de hijos, educación y nivel de ingresos.  
- Evaluar el comportamiento multicanal.  
- Detectar los productos con mayor ticket medio.  

**Herramientas utilizadas:**  
- Python (Limpieza y preparación de los datos).
- BigQuery (almacenamiento y preparación de los datos).
- Power BI (modelado, DAX, visualizaciones).  
  
**Principales insights:**  
- Alta proporción de clientes multicanal.  
- Vinos y carnes concentran gran parte del ticket medio.  
- Diferencias claras en el gasto según perfil demográfico.  

**Vista previa:**  
![Dashboard de Marketing](resumen.png)
![Dashboard de Marketing](Canales.png)

**Ver más:**  
### 📂 Detalle del proyecto
- 📊 [Dataset (CSV)](marketing_campaign.csv)  
- 🐍 [Script en Python](analisis_marketing.py)  
- 🗄️ [Consultas SQL](marketing_cleaning_queries.sql)  
- 📑 [Archivo Power BI](Proyecto_Marketing.pbix)

### 2. Análisis de Airbnb en Madrid
**Descripción:**  
Este proyecto analiza datos de alojamientos de Airbnb en Madrid utilizando Python para la limpieza y análisis exploratorio, y Power BI para el modelado y visualización de los resultados.

**Objetivos:**  
- Analizar la distribución de propiedades por distrito y tipo de alojamiento.  
- Identificar variaciones en el precio medio por noche según ubicación.  
- Detectar outliers en los precios y normalizar los datos.  
- Evaluar la disponibilidad y reseñas a lo largo del tiempo.  

**Herramientas utilizadas:**  
- Python (Pandas, Matplotlib, Seaborn, Numpy) → limpieza y análisis exploratorio.
- Power BI → modelado, medidas DAX y visualizaciones interactivas.
- Excel/CSV → dataset de Airbnb con alojamientos en Madrid.  

**Principales insights:**  
- Los apartamentos concentran la mayor parte de la oferta frente a otros tipos de propiedades.  
- Diferencias significativas en el precio promedio por distrito.  
- Presencia de outliers extremos en los precios que distorsionaban los resultados.
- Los barrios céntricos tienen mayor disponibilidad, aunque con precios más altos. 

**Vista previa:**  
![Airbnb_Madrid](Airbnb_dashboard.png)

**Ver más:**  
### 📂 Detalle del proyecto
- 📊 [Dataset (CSV)](listings.csv)  
- 🐍 [Script en Python](airbnb_cleaning.py)    
- 📑 [Archivo Power BI](Airbnb_Madrid.pbix)

### 3.Hotel Booking Analysis — Data Cleaning & Insights
Análisis exploratorio y de comportamiento de cancelaciones en reservas hoteleras

1. Descripción del Proyecto

Este proyecto analiza el dataset Hotel Booking Demand con el objetivo de comprender los patrones de cancelación de reservas según distintos factores: país, tipo de cliente, canal de reserva, tipo de depósito, entre otros.
Se aplican técnicas de limpieza de datos, análisis exploratorio (EDA) y generación de hipótesis e insights útiles para la toma de decisiones.

2. Librerías Principales

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Configuraciones de visualización:
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid', palette='muted')

3. Limpieza y Preparación de Datos

1️⃣ Carga y exploración inicial

- Se observó tamaño del dataset, tipos de datos y valores nulos.
- Se eliminaron duplicados.
- Se imputaron valores faltantes con criterios representativos.

df = pd.read_csv('hotel_bookings.csv')
df = df.drop_duplicates()
df['agent'] = df['agent'].fillna('Unknown')
df['company'] = df['company'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['children'] = df['children'].fillna(0).astype(int)

2️⃣ Feature Engineering

- stay_length: duración total de la estancia.
- high_season: indicador de temporada alta.
- year y month: extracción de fecha de reserva.
- high_season_arrival: temporada alta al momento del arribo.

df['stay_length'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
df['month'] = df['reservation_status_date'].dt.month
df['year'] = df['reservation_status_date'].dt.year
df['high_season'] = df['month'].isin([6,7,8,12]).astype(int)

4. Análisis Exploratorio (EDA)
🔹 Distribución general de reservas

- City Hotel concentra más reservas que Resort Hotel, pero tiene mayor tasa de cancelación.
sns.countplot(x='hotel', data=df)
plt.title('Distribución de reservas por tipo de hotel')
plt.show()

- Las reservas se concentran en meses de verano (junio-agosto) y diciembre.
- La tasa global de cancelación es aproximadamente 27%.

🔹 Duración de la estancia por tipo de cliente

sns.barplot(x='customer_type', y='stay_length', data=df)
plt.title('Duración promedio de estancia por tipo de cliente')
plt.show()

📍 Insight:
Los clientes Transient (individuales) tienden a estancias más cortas, mientras que los Group tienen estancias más largas.

🔹 Relación entre precio (ADR) y cancelaciones

sns.barplot(x='is_canceled', y='adr', data=df)
plt.title('Precio promedio (ADR) según cancelación')
plt.show()

📍 Insight:
Las reservas canceladas presentan ADR ligeramente más alto, lo cual puede indicar búsqueda de precios más competitivos o reubicaciones posteriores.

5. Análisis de Cancelaciones
5.1 Cancelaciones por Segmento

Para cada variable categórica (hotel, country, market_segment, distribution_channel, etc.) se calcularon:
- Total de reservas
- Total de cancelaciones
- Tasa (%) de cancelación
- Promedio de noches por reserva

def resumen_cancelaciones_mejorado(df, columna):
    resumen = (
        df.groupby(columna)
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            noches_promedio=('stay_length', 'mean')
        )
    )
    resumen['tasa_cancelacion'] = (resumen['tasa_cancelacion'] * 100).round(1)
    resumen['noches_promedio'] = resumen['noches_promedio'].round(1)
    return resumen.sort_values(by=['reservas', 'tasa_cancelacion'], ascending=[False, False])

📍 Conclusiones principales:
- City Hotel presenta más cancelaciones que Resort Hotel.
- Portugal domina en volumen y tasa de cancelación (35,7%).
- España tiene tasas altas a pesar de su ADR más elevado.
- Segmentos online presentan más cancelaciones (mayor flexibilidad).
- A mayor duración de estancia, aumenta la tasa de cancelación (contrario a lo esperado).

5.2 Clientes con historial de cancelaciones

df['previous_cancel_group'] = df['previous_cancellations'].apply(
    lambda x: 'No canceló antes' if x == 0 else 'Canceló antes'
)

📍 Insight:
Los clientes que ya cancelaron previamente presentan una tasa de cancelación actual más alta → se confirma un comportamiento repetitivo.

5.3 Cambio de habitación y cancelaciones

df['room_changed'] = (df['reserved_room_type'] != df['assigned_room_type']).astype(int)

📍 Insight:
No se encontró una relación significativa entre el cambio de habitación y la cancelación (solo 4% de las reservas cambiadas terminan canceladas).

6. Comparativa Internacional

comparacion_paises = (
    df[df['country'].isin(['PRT','ESP','FRA','GBR','DEU'])]
    .groupby('country')
    .agg(
        reservas=('is_canceled', 'count'),
        cancelaciones=('is_canceled', 'sum'),
        tasa_cancelacion=('is_canceled', 'mean'),
        adr_promedio=('adr', 'mean')
    )
)

Resumen:

| País | Reservas | Cancelaciones | Tasa (%) | ADR (€) |
| ---- | -------- | ------------- | -------- | ------- |
| PRT  | 27,453   | 9,791         | 35.7     | 95.84   |
| ESP  | 7,252    | 1,862         | 25.7     | 122.28  |
| FRA  | 8,837    | 1,733         | 19.6     | 112.53  |
| DEU  | 5,387    | 1,053         | 19.5     | 105.94  |
| GBR  | 10,433   | 1,985         | 19.0     | 97.67   |


Correlación ADR vs Tasa de Cancelación: −0.25
→ Leve tendencia inversa, no universal.

🔸 País + Canal

En España, las cancelaciones son muy altas en el canal online.
En Portugal, tanto el canal offline como online tienen tasas cercanas al 43%.

🔸 País + Tipo de Depósito

Predomina “No Deposit”.
Portugal tiene un volumen significativo de “Non Refund” con 97% de cancelaciones → probable inconsistencia o error de clasificación.

🔸 País + Tipo de Cliente

Portugal concentra muchos clientes Transient-Party, con alta cancelación (33,3%) y ADR bajo.
Refleja un patrón de grupos informales o familiares que tienden a modificar o cancelar reservas con mayor frecuencia.

7. Conclusiones Generales

Portugal impulsa la tasa global de cancelación del dataset.
Las cancelaciones se asocian más a canales online y estancias medias/largas.
Clientes reincidentes son más propensos a volver a cancelar.
No se observa relación significativa entre cambio de habitación y cancelación.
La relación entre precio (ADR) y cancelación es débilmente inversa (−0.25).

---

## 🛠️ Herramientas que utilizo
- **Power BI** → Dashboards interactivos y DAX.    
- **SQL** → Consultas y modelado de bases de datos.  
- **Excel** → Reporting y análisis rápido.
- **Python** → Limpieza y análisis de datos (Pandas, Matplotlib, Seaborn).

---

## 📬 Contacto
- 💼 [LinkedIn](https://www.linkedin.com/in/ezequielbochicchio/) 
- 📧 [Email](mailto:ezequiel.bochicchio88@gmail.com)  
- 🐙 [GitHub](https://github.com/ezequielbochicchio88-collab)  

---
✍️ *Este portfolio está en constante actualización con nuevos proyectos.*
