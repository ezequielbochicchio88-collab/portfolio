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
**Análisis exploratorio y de comportamiento de cancelaciones en reservas hoteleras**

**1. Descripción del Proyecto**

Este proyecto analiza el dataset Hotel Booking Demand con el objetivo de comprender los patrones de cancelación de reservas según distintos factores: país, tipo de cliente, canal de reserva, tipo de depósito, entre otros.
Se aplican técnicas de limpieza de datos, análisis exploratorio (EDA) y generación de hipótesis e insights útiles para la toma de decisiones.

**2. Limpieza y Preparación de Datos**

**1️⃣ Carga y exploración inicial**

- Se observó tamaño del dataset, tipos de datos y valores nulos.
- Se eliminaron duplicados.
- Se imputaron valores faltantes con criterios representativos.

**2️⃣ Feature Engineering**

- stay_length: duración total de la estancia.
- high_season: indicador de temporada alta.
- year y month: extracción de fecha de reserva.
- high_season_arrival: temporada alta al momento del arribo.

**3. Análisis Exploratorio (EDA)**
**🔹 Distribución general de reservas**

- City Hotel concentra más reservas que Resort Hotel, pero tiene mayor tasa de cancelación.
- Las reservas se concentran en meses de verano (julio-agosto).
- La tasa global de cancelación es aproximadamente 27%.

<img width="1218" height="894" alt="image" src="https://github.com/user-attachments/assets/ab2c8189-0323-4a3d-83a5-31641b5f3fb7" />
<img width="1310" height="920" alt="image" src="https://github.com/user-attachments/assets/3b3ce4f9-fecf-42ca-8c67-cb40ec3b93a9" />

**🔹 Duración de la estancia por tipo de cliente**

**📍 Insight:**
Los clientes Transient (individuales) tienden a estancias más cortas, mientras que los Group tienen estancias más largas.
<img width="1604" height="1134" alt="image" src="https://github.com/user-attachments/assets/2c13c31f-caf1-4172-9928-6e95cd52d478" />

**🔹 Relación entre precio (ADR) y cancelaciones**

**📍 Insight:**
Las reservas canceladas presentan ADR ligeramente más alto, lo cual puede indicar búsqueda de precios más competitivos o reubicaciones posteriores.

**4. Análisis de Cancelaciones**
**4.1 Cancelaciones por Segmento**

Para cada variable categórica (hotel, country, market_segment, distribution_channel, etc.) se calcularon:
- Total de reservas
- Total de cancelaciones
- Tasa (%) de cancelación
- Promedio de noches por reserva

**📍 Conclusiones principales:**
- City Hotel presenta más cancelaciones que Resort Hotel.
- Portugal domina en volumen y tasa de cancelación (35,7%).
- España tiene tasas altas a pesar de su ADR más elevado.
- Segmentos online presentan más cancelaciones (mayor flexibilidad).
- A mayor duración de estancia, aumenta la tasa de cancelación (contrario a lo esperado).

**4.2 Clientes con historial de cancelaciones**

**📍 Insight:**
Los clientes que ya cancelaron previamente presentan una tasa de cancelación actual más alta → se confirma un comportamiento repetitivo.

**4.3 Cambio de habitación y cancelaciones**

**📍 Insight:**
No se encontró una relación significativa entre el cambio de habitación y la cancelación (solo 4% de las reservas cambiadas terminan canceladas).

**5. Comparativa Internacional**

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

**🔸 País + Canal**

- En España, las cancelaciones son muy altas en el canal online.
- En Portugal, tanto el canal offline como online tienen tasas cercanas al 43%.

**🔸 País + Tipo de Depósito**

- Predomina “No Deposit”.
- Portugal tiene un volumen significativo de “Non Refund” con 97% de cancelaciones → probable inconsistencia o error de clasificación.

**🔸 País + Tipo de Cliente**

- Portugal concentra muchos clientes Transient-Party, con alta cancelación (33,3%) y ADR bajo.
- Refleja un patrón de grupos informales o familiares que tienden a modificar o cancelar reservas con mayor frecuencia.

**6. Conclusiones Generales**

- Portugal impulsa la tasa global de cancelación del dataset.
- Las cancelaciones se asocian más a canales online y estancias medias/largas.
- Clientes reincidentes son más propensos a volver a cancelar.
- No se observa relación significativa entre cambio de habitación y cancelación.
- La relación entre precio (ADR) y cancelación es débilmente inversa (−0.25).

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
