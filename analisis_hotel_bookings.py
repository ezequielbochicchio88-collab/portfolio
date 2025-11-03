# ================================================
# Analisis Hotel Bookings - Limpieza y EDA
# Generado por ChatGPT para Ezequiel Bochicchio
# ================================================

# --- Librerías principales ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# --- Configuraciones de visualización ---
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid', palette='muted')

# --- Ajustar ruta del dataset si hace falta ---
DATA_PATH = r'/Users/ezequielbochicchio/Desktop/Python/Booking/hotel_bookings.csv'

def main():
    # Cargar dataset
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo en {DATA_PATH}. Ajusta DATA_PATH en el script.")
        sys.exit(1)

    # Dimensiones y primeras filas
    print("Dimensiones:", df.shape)
    print(df.head().to_string(index=False))

    # Información general
    print('\n--- Info del dataframe ---')
    df.info()

    # Resumen estadístico general (muestra parcial)
    print('\n--- Resumen estadístico (head) ---')
    print(df.describe(include='all').T.head(20).to_string())

    # Conteo de valores nulos
    print('\n--- Valores nulos por columna ---')
    print(df.isna().sum().sort_values(ascending=False).to_string())

    # Duplicados por columna
    print('\n--- Duplicados por columna ---')
    for col in df.columns:
        total = len(df[col])
        unicos = df[col].nunique(dropna=False)
        duplicados = total - unicos
        print(f"{col}: {duplicados} duplicados")


    # Filas duplicadas completas
    duplicated_rows = df[df.duplicated()]
    print(f"\nFilas duplicadas completas: {duplicated_rows.shape[0]}")
    if duplicated_rows.shape[0] > 0:
        print(duplicated_rows.head().to_string())

    # Eliminar duplicados si existen
    duplicados = df.duplicated().sum()
    print(f"\nFilas duplicadas (total): {duplicados}")
    if duplicados > 0:
        df = df.drop_duplicates().reset_index(drop=True)
        print(f"✅ Filas duplicadas eliminadas. Nuevo tamaño: {df.shape}")
    else:
        print("✅ No se encontraron filas duplicadas.")

    # Imputación de nulos simples
    df['agent'] = df['agent'].fillna('Unknown')
    df['company'] = df['company'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['children'] = df['children'].fillna(0).astype(int)

    # Conversión de fechas y nuevas variables
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], errors='coerce')
    df['stay_length'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
    df['month'] = df['reservation_status_date'].dt.month
    df['year'] = df['reservation_status_date'].dt.year
    df['high_season'] = df['month'].isin([6,7,8,12]).astype(int)

    # --- Gráficos exploratorios ---
    plt.figure(figsize=(8,5))
    sns.countplot(x='hotel', data=df)
    plt.title('Distribución de reservas por tipo de hotel')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8,5))
    sns.countplot(x='month', data=df)
    plt.title('Distribución de reservas por mes en el que se hace la reserva')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,5))
    sns.countplot(x='arrival_date_month', data=df, order=df['arrival_date_month'].value_counts().index)
    plt.title('Distribución de reservas por mes de llegada')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6,4))
    sns.countplot(x='high_season', data=df)
    plt.title('Distribución de reservas según temporada alta y baja')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,5))
    sns.countplot(x='market_segment', data=df)
    plt.title('Distribución de reservas según segmento de mercado')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8,5))
    sns.countplot(x='customer_type', data=df)
    plt.title('Distribución de reservas según tipo de cliente')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Top 10 países con más reserva
    top_countries = df['country'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top_countries.values, y=top_countries.index)
    plt.title('Top 10 países con más reservas')
    plt.xlabel('Reservas')
    plt.tight_layout()
    plt.show()

    # Alta temporada de llegada (ejemplo)
    df['high_season_arrival'] = df['arrival_date_month'].isin(["July","August","September","December"]).astype(int)
    plt.figure(figsize=(6,4))
    sns.countplot(x='high_season_arrival', data=df)
    plt.title('Distribución de reservas según temporada alta y baja (llegada)')
    plt.tight_layout()
    plt.show()

    # Porcentaje de cancelaciones
    cancel_rate = df['is_canceled'].mean() * 100
    print(f"\nTasa de cancelaciones: {cancel_rate:.2f}%")
    plt.figure(figsize=(6,4))
    sns.countplot(x='is_canceled', data=df)
    plt.title('Cancelaciones vs Reservas efectivas')
    plt.tight_layout()
    plt.show()

    # Duración de estancia por tipo de cliente (barras)
    plt.figure(figsize=(8,6))
    order = df.groupby('customer_type')['stay_length'].mean().sort_values(ascending=False).index
    sns.barplot(x='customer_type', y='stay_length', data=df, color='lightblue', ci=None, order=order)
    plt.title('Duración promedio de estancia por tipo de cliente')
    plt.xlabel('Tipo de cliente')
    plt.ylabel('Duración promedio (noches)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Relación entre precio (ADR) y cancelaciones
    plt.figure(figsize=(7,5))
    order_cancel = df.groupby('is_canceled')['adr'].mean().sort_values(ascending=False).index
    ax = sns.barplot(x='is_canceled', y='adr', data=df, color='skyblue', ci=None, order=order_cancel)
    for container in ax.containers:
        ax.bar_label(container, fmt='%.2f', label_type='edge', fontsize=9)
    plt.title('Precio promedio (ADR) según cancelación')
    plt.xlabel('Cancelación (0 = No, 1 = Sí)')
    plt.ylabel('Precio promedio (ADR)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Agrupación por duración de estancia ---
    bins = [0, 1, 4, 7, df['stay_length'].max()]
    labels = ['0–1 noche', '2–4 noches', '5–7 noches', 'Más de 7 noches']
    df['stay_length_group'] = pd.cut(df['stay_length'], bins=bins, labels=labels, include_lowest=True)

    # Función resumen
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
        resumen = resumen.sort_values(by=['reservas', 'tasa_cancelacion'], ascending=[False, False])
        return resumen

    variables = [
        'hotel', 'country', 'market_segment', 'distribution_channel',
        'is_repeated_guest', 'deposit_type', 'company', 'customer_type',
        'stay_length_group'
    ]

    for col in variables:
        print(f"\n📈 Cancelaciones por {col.upper()}:")
        print(resumen_cancelaciones_mejorado(df, col).to_string())

    # --- Cancelaciones previas ---
    df['previous_cancel_group'] = df['previous_cancellations'].apply(lambda x: 'No canceló antes' if x == 0 else 'Canceló antes')
    cancel_prev_grouped = (
        df.groupby('previous_cancel_group')['is_canceled']
        .agg(['count', 'sum', 'mean'])
        .rename(columns={'count': 'reservas', 'sum': 'cancelaciones_actuales', 'mean': 'tasa_cancelacion_actual'})
    )
    cancel_prev_grouped['tasa_cancelacion_actual'] = (cancel_prev_grouped['tasa_cancelacion_actual'] * 100).round(1)

    print("\n📊 Relación entre cancelaciones previas (agrupadas) y cancelación actual:")
    print(cancel_prev_grouped.to_string())

    plt.figure(figsize=(6,5))
    sns.barplot(x=cancel_prev_grouped.index, y='tasa_cancelacion_actual', data=cancel_prev_grouped.reset_index(), color='skyblue')
    plt.title('Tasa de cancelación actual según historial previo')
    plt.ylabel('Tasa de cancelación actual (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Cambio de habitación ---
    df['room_changed'] = (df['reserved_room_type'] != df['assigned_room_type']).astype(int)
    room_cancel = (
        df.groupby('room_changed')['is_canceled']
        .agg(['count', 'sum', 'mean'])
        .rename(columns={'count': 'reservas', 'sum': 'cancelaciones', 'mean': 'tasa_cancelacion'})
    )
    room_cancel['tasa_cancelacion'] = (room_cancel['tasa_cancelacion'] * 100).round(1)
    print("\n📊 Relación entre cambio de habitación y cancelaciones:")
    print(room_cancel.to_string())

    plt.figure(figsize=(6,5))
    sns.barplot(x=['Misma habitación', 'Distinta habitación'], y='tasa_cancelacion', data=room_cancel.reset_index(), color='lightcoral')
    plt.title('Tasa de cancelación según cambio de habitación')
    plt.ylabel('Tasa de cancelación (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Comparación por países seleccionados ---
    paises_clave = ['PRT', 'ESP', 'FRA', 'GBR', 'DEU']
    df_paises = df[df['country'].isin(paises_clave)]

    comparacion_paises = (
        df_paises.groupby('country')
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            adr_promedio=('adr', 'mean')
        )
    )
    comparacion_paises['tasa_cancelacion'] = (comparacion_paises['tasa_cancelacion'] * 100).round(1)
    comparacion_paises['adr_promedio'] = comparacion_paises['adr_promedio'].round(2)
    comparacion_paises = comparacion_paises.round({'reservas': 0, 'cancelaciones': 0})
    comparacion_paises = comparacion_paises.sort_values(by='tasa_cancelacion', ascending=False)

    print("\n📊 Comparación entre países seleccionados:")
    print(comparacion_paises.to_string())

    plt.figure(figsize=(8,5))
    sns.scatterplot(x='adr_promedio', y='tasa_cancelacion', data=comparacion_paises, s=150, color='steelblue')
    for i, country in enumerate(comparacion_paises.index):
        plt.text(comparacion_paises['adr_promedio'][i] + 0.2, comparacion_paises['tasa_cancelacion'][i] + 0.3, country, fontsize=10)
    plt.title('Relación entre precio promedio (ADR) y tasa de cancelación')
    plt.xlabel('ADR promedio (€)')
    plt.ylabel('Tasa de cancelación (%)')
    plt.grid(alpha=0.5, linestyle='--')
    plt.tight_layout()
    plt.show()

    correlacion = comparacion_paises['adr_promedio'].corr(comparacion_paises['tasa_cancelacion'])
    print(f"🔗 Correlación ADR vs Tasa de cancelación: {correlacion:.2f}")

    # --- Relación país + canal ---
    resumen_pais_canal = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'market_segment'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            adr_promedio=('adr', 'mean')
        )
    )
    resumen_pais_canal['tasa_cancelacion'] = (resumen_pais_canal['tasa_cancelacion'] * 100).round(1)
    print(resumen_pais_canal.sort_values(by=['country', 'tasa_cancelacion'], ascending=[True, False]).to_string())

    # --- Relación país + depósito ---
    resumen_pais_deposito = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'deposit_type'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            adr_promedio=('adr', 'mean')
        )
    )
    resumen_pais_deposito['tasa_cancelacion'] = (resumen_pais_deposito['tasa_cancelacion'] * 100).round(1)
    resumen_pais_deposito['adr_promedio'] = resumen_pais_deposito['adr_promedio'].round(2)
    print("\n💰 Relación entre país, tipo de depósito y cancelaciones:")
    print(resumen_pais_deposito.sort_values(by=['country', 'tasa_cancelacion'], ascending=[True, False]).to_string())

    # --- Relación país + tipo de cliente ---
    resumen_pais_cliente = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'customer_type'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            adr_promedio=('adr', 'mean')
        )
    )
    resumen_pais_cliente['tasa_cancelacion'] = (resumen_pais_cliente['tasa_cancelacion'] * 100).round(1)
    resumen_pais_cliente['adr_promedio'] = resumen_pais_cliente['adr_promedio'].round(2)
    print("\n👥 Relación entre país, tipo de cliente y cancelaciones:")
    print(resumen_pais_cliente.sort_values(by=['country', 'tasa_cancelacion'], ascending=[True, False]).to_string())

    # --- Cruzado Portugal: customer_type x market_segment ---
    pt_cliente_segmento = (
        df[df['country'] == 'PRT']
        .groupby(['customer_type', 'market_segment'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean'),
            adr_promedio=('adr', 'mean')
        )
    )
    pt_cliente_segmento['tasa_cancelacion'] = (pt_cliente_segmento['tasa_cancelacion'] * 100).round(1)
    pt_cliente_segmento['adr_promedio'] = pt_cliente_segmento['adr_promedio'].round(2)
    print("\n🇵🇹 Portugal — Cancelaciones por tipo de cliente y segmento de mercado:")
    print(pt_cliente_segmento.sort_values(by='tasa_cancelacion', ascending=False).to_string())

    # --- Visualización combinada país x canal / depósito / cliente ---
    sns.set(style="whitegrid", palette="Set2")
    resumen_canal = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'market_segment'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean')
        )
        .reset_index()
    )
    resumen_canal['tasa_cancelacion'] = (resumen_canal['tasa_cancelacion'] * 100).round(1)

    resumen_deposito = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'deposit_type'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean')
        )
        .reset_index()
    )
    resumen_deposito['tasa_cancelacion'] = (resumen_deposito['tasa_cancelacion'] * 100).round(1)

    resumen_cliente = (
        df[df['country'].isin(paises_clave)]
        .groupby(['country', 'customer_type'])
        .agg(
            reservas=('is_canceled', 'count'),
            cancelaciones=('is_canceled', 'sum'),
            tasa_cancelacion=('is_canceled', 'mean')
        )
        .reset_index()
    )
    resumen_cliente['tasa_cancelacion'] = (resumen_cliente['tasa_cancelacion'] * 100).round(1)

    fig, axes = plt.subplots(3, 1, figsize=(10, 16))
    fig.suptitle("Tasa de Cancelación (%) por País y Segmento de Análisis", fontsize=16, fontweight="bold")

    sns.barplot(data=resumen_canal, x='country', y='tasa_cancelacion', hue='market_segment', ax=axes[0])
    axes[0].set_title("Por Canal de Distribución")
    axes[0].set_ylabel("Tasa de Cancelación (%)")
    axes[0].legend(title="Canal", bbox_to_anchor=(1.05, 1), loc='upper left')

    sns.barplot(data=resumen_deposito, x='country', y='tasa_cancelacion', hue='deposit_type', ax=axes[1])
    axes[1].set_title("Por Tipo de Depósito")
    axes[1].set_ylabel("Tasa de Cancelación (%)")
    axes[1].legend(title="Tipo de Depósito", bbox_to_anchor=(1.05, 1), loc='upper left')

    sns.barplot(data=resumen_cliente, x='country', y='tasa_cancelacion', hue='customer_type', ax=axes[2])
    axes[2].set_title("Por Tipo de Cliente")
    axes[2].set_ylabel("Tasa de Cancelación (%)")
    axes[2].legend(title="Tipo de Cliente", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()

if __name__ == '__main__':
    main()
