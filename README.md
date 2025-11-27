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

Se aplican técnicas de limpieza de datos, análisis exploratorio (EDA) y generación de hipótesis e insights útiles para la toma de decisiones, mediante el uso de Python.

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
Los clientes Transient (individuales) tienden a estancias más cortas, mientras que los Contract (empleados que son enviados por una empresa por ejemplo) tienen estancias más largas.

<img width="1604" height="1134" alt="image" src="https://github.com/user-attachments/assets/2c13c31f-caf1-4172-9928-6e95cd52d478" />

**🔹 Relación entre precio (ADR) y cancelaciones**

**📍 Insight:**
Las reservas canceladas presentan ADR ligeramente más alto, lo cual puede indicar búsqueda de precios más competitivos o reubicaciones posteriores.

<img width="1394" height="960" alt="image" src="https://github.com/user-attachments/assets/7f477c1b-bc03-4c58-8e10-44aaad72d4cc" />

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

<img width="1106" height="316" alt="image" src="https://github.com/user-attachments/assets/63e98d9b-9e0d-452b-9bbd-32fe96abc007" />
<img width="1024" height="464" alt="image" src="https://github.com/user-attachments/assets/2788fb07-4810-49bb-a6bb-67d54ac16219" />
<img width="1196" height="664" alt="image" src="https://github.com/user-attachments/assets/6932c7cc-b1cd-411b-a7c2-d3d572e08e52" />
<img width="1170" height="360" alt="image" src="https://github.com/user-attachments/assets/33019797-f3c1-418e-96a1-02bcb7e5d1f5" />

**4.2 Clientes con historial de cancelaciones**

**📍 Insight:**
Los clientes que ya cancelaron previamente presentan una tasa de cancelación actual más alta → se confirma un comportamiento repetitivo.

<img width="1194" height="290" alt="image" src="https://github.com/user-attachments/assets/e00ad02f-fa12-480c-9436-3d9adb525672" />

**4.3 Cambio de habitación y cancelaciones**

**📍 Insight:**
No se encontró una relación significativa entre el cambio de habitación y la cancelación (solo 4% de las reservas cambiadas terminan canceladas).

<img width="898" height="276" alt="image" src="https://github.com/user-attachments/assets/788ace24-405a-4fa4-9a33-b9761786a48b" />

**5. Comparativa Internacional**

Resumen:

| País | Reservas | Cancelaciones | Tasa (%) | ADR (€) |
| ---- | -------- | ------------- | -------- | ------- |
| PRT  | 27,453   | 9,791         | 35.7     | 95.84   |
| ESP  | 7,252    | 1,862         | 25.7     | 122.28  |
| FRA  | 8,837    | 1,733         | 19.6     | 112.53  |
| DEU  | 5,387    | 1,053         | 19.5     | 105.94  |
| GBR  | 10,433   | 1,985         | 19.0     | 97.67   |

<img width="1592" height="946" alt="image" src="https://github.com/user-attachments/assets/500d76c7-b652-4245-bf1f-9db9471a3bdd" />

Correlación ADR vs Tasa de Cancelación: −0.25
→ Leve tendencia inversa, no universal.

**🔸 País + Canal**

- En España, las cancelaciones son muy altas en el canal online.
- En Portugal, tanto el canal offline como online tienen tasas cercanas al 43%.

<img width="2032" height="1132" alt="image" src="https://github.com/user-attachments/assets/5be889ac-94a5-4691-85c6-3ad5fb49078a" />

**🔸 País + Tipo de Depósito**

- Predomina “No Deposit”.
- Portugal tiene un volumen significativo de “Non Refund” con 97% de cancelaciones → probable inconsistencia o error de clasificación.

<img width="1986" height="1008" alt="image" src="https://github.com/user-attachments/assets/464d26a4-9746-4a64-afcd-c07ec80c8e09" />

**🔸 País + Tipo de Cliente**

- Portugal concentra muchos clientes Transient-Party, con alta cancelación (33,3%) y ADR bajo.
- Refleja un patrón de grupos informales o familiares que tienden a modificar o cancelar reservas con mayor frecuencia.

<img width="1986" height="990" alt="image" src="https://github.com/user-attachments/assets/797e196d-8d4c-46de-a693-88b2b215fca6" />

**6. Conclusiones Generales**

- Portugal impulsa la tasa global de cancelación del dataset.
- Las cancelaciones se asocian más a canales online y estancias medias/largas.
- Clientes reincidentes son más propensos a volver a cancelar.
- No se observa relación significativa entre cambio de habitación y cancelación.
- La relación entre precio (ADR) y cancelación es débilmente inversa (−0.25).

**Ver más:**  
### 📂 Detalle del proyecto
- 📊 [Dataset (CSV)](hotel_booking.csv)
- 📊 [Dataset post limpieza y transformaciones](hotel_booking_clean.csv) 
- 🐍 [Script en Python](analisis_hotel_bookings.py)  

### 4.BMW Sales Data — Business Case with SQL 
**Análisis de las ventas de BMW a nivel global entre el año 2010 y 2024**

**1. Descripción del Proyecto**

Este proyecto analiza el dataset BMW sales data (2010-2024) con el objetivo de responder, mediante el uso de consultas SQL, diversas preguntas estilo Business Case planteadas por ChatGPT.

Se aplican técnicas de limpieza y transformación de datos mediante el uso de Python para luego cargar el dataset limpio en Google BigQuery y comenzar el analisis y las respuestas a todas las preguntas planteadas, usando solamente consultas SQL.

**2. Limpieza y Preparación de Datos**

**1️⃣ Carga y exploración inicial**

- Se observó tamaño del dataset, tipos de datos, valores nulos y redondeo de campos númericos.

**2️⃣ Feature Engineering**

- year
- Price_per_liter: precio / tamaño del motor.
- Price_per_KM: precio / kilometraje.
- Revenue_USD: Precio * volumen de venta.

**3. Análisis en Google BigQuery**

🏁 I. Rendimiento General de Ventas
1️⃣ Evolución del volumen total de ventas

Intención: Analizar tendencias anuales y detectar años de crecimiento o caída.
Resultado:
- Entre 2011 y 2015 el volumen de ventas aumentó de 16M a 17M unidades, pero luego comenzó a decrecer hasta 2019, año en el que volvió a alcanzar los niveles de 2015.
- En 2020 se registró el mínimo histórico (16,3M), probablemente debido al impacto del Covid-19.
- Desde 2021 las ventas se recuperaron, alcanzando su pico máximo en 2022 con 17,9M unidades.

2️⃣ Modelos que más aportan al total de ingresos globales

Intención: Identificar los modelos más rentables, no solo los más vendidos.
Resultado:
- Los 5 modelos más rentables (por total de ingresos) son:

7 Series
3 Series
I8
X1
5 Series

3️⃣ Región con mayor porcentaje de ventas totales

Intención: Evaluar la distribución geográfica y el peso relativo de cada región.
Resultado:
- Aunque el volumen de ventas es relativamente homogéneo entre regiones, Asia lidera con cerca del 17% del total global.

🌍 II. Análisis Geográfico
4️⃣ Región más rentable por tipo de combustible

Intención: Evaluar qué combustibles funcionan mejor en cada mercado.
Resultado:

- Petrol: Middle East
- Hybrid: Asia
- Diesel: Asia
- Electric: North America

5️⃣ Precio promedio más alto por tamaño de motor y región

Intención: Determinar si los motores grandes se valoran más en ciertos mercados.
Resultado:

- Small: África
- Medium: Sudamérica
- Large: Asia
- Performance: Asia

6️⃣ Color de automóvil más vendido por continente

Intención: Conocer preferencias estéticas regionales.
Resultado: (visualización pendiente)

⚙️ III. Producto y Segmentación
7️⃣ Modelos dominantes en cada segmento de ventas (“High”, “Medium”, “Low”)

Intención: Identificar qué productos lideran cada nivel comercial.
Resultado:
- El BMW 7 Series domina tanto el segmento High como el Low en función del volumen de ventas.

8️⃣ Impacto de la transmisión en precio y volumen de ventas

Intención: Entender si los clientes pagan más por transmisiones automáticas.
Resultado:
- Los coches con transmisión automática tienen un precio promedio más alto y mayor volumen de ventas que los manuales, especialmente impulsados por Europa y Norteamérica.

9️⃣ Correlación entre tamaño del motor, precio y ventas

Intención: Verificar si los motores grandes impulsan ventas o solo precios.
Resultado:
- Los vehículos con motores grandes muestran el mayor volumen de ventas promedio y los precios más altos, aunque en menor cantidad dentro del dataset.

⛽ IV. Tendencias por Tipo de Combustible
🔟 Combustibles con mayor crecimiento de participación

Intención: Analizar la transición hacia híbridos o eléctricos.
Resultado:
- Los Diesel e Híbridos son los tipos de combustible que más ganaron cuota de mercado entre 2010 y 2024.
- Además, ambos aumentaron significativamente su volumen de ventas, mientras que los eléctricos y gasolina perdieron participación.

11️⃣ Combinación modelo + tipo de combustible más rentable

Intención: Detectar oportunidades comerciales (p. ej., híbridos de alta gama).
Resultado:
- La combinación BMW 7 Series Híbrido es la que mayor nivel de ingresos genera a nivel global.

📈 V. Desempeño Financiero
12️⃣ Modelos con mayor precio promedio por litro de motor

Intención: Medir la eficiencia económica del tamaño del motor.
Resultado: (visualización pendiente)

🧩 VI. Análisis Combinado y Avanzado
14️⃣ Modelos con ventas altas pese a precios superiores al promedio

Intención: Detectar productos de alta demanda que no dependen de descuentos.
Resultado: (visualización pendiente)

15️⃣ Regiones o modelos con señales de saturación

Intención: Detectar mercados maduros o productos en declive.
Resultado:
- El top 5 de combinaciones modelo/región con ventas decrecientes muestra señales de saturación, indicando posibles mercados maduros o productos a revisar.

🧠 BONUS — Preguntas Estratégicas Tipo Business Case Real
1️⃣ Inversión publicitaria por región y tipo de combustible

Análisis:

- Asia: crecimiento sostenido tanto en ventas como en revenue → región prioritaria.
- North America: crecimiento moderado en ventas, pero fuerte aumento en rentabilidad.
- Combustibles: priorizar Híbridos, seguidos por Eléctricos.

2️⃣ Modelos a discontinuar o reemplazar

Análisis:
Modelos con caídas continuas en ventas y rentabilidad en los últimos años. (visualización pendiente)

3️⃣ Segmento de motor con mejor margen por unidad vendida

Análisis:
- Los vehículos con motores grandes generan el mayor margen promedio por unidad.

4️⃣ “Sweet spot” de precio que maximiza el volumen de ventas

Análisis:
- El rango 30K–50K USD representa el punto óptimo de ventas, combinando alto volumen y rentabilidad equilibrada.

🏁 Conclusión

Este análisis integral de BMW (2010–2024) combina tendencias de ventas, rentabilidad y comportamiento del consumidor para:
- Detectar modelos con potencial de crecimiento o declive.
- Identificar mercados estratégicos por región y combustible.
- Establecer rangos de precio óptimos y segmentos de motor más rentables.
- Guiar decisiones sobre innovación, marketing y discontinuación de producto.

  
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
