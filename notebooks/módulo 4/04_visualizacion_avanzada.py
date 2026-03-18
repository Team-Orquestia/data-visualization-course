import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

st.set_page_config(layout="wide")
st.title("Visualización de Datos en Streamlit")

# Generamos datos sintéticos
# -------------------------
np.random.seed(42)
df = pd.DataFrame(
    np.random.randn(50, 3) + [1, 2, 3],
    columns=['A', 'B', 'C']
)
df['categoria'] = np.random.choice(['X', 'Y', 'Z'], 50)
df['fecha'] = pd.date_range('2023-01-01', periods=50)

# 1. Gráficos Nativos y Rápidos (st.bar_chart, st.line_chart, st.area_chart)
st.header("1. Gráficos Nativos Básicos")
st.write("Streamlit tiene envoltorios muy simples para gráficos rápidos (basados en Altair).")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Gráfico de Líneas")
    st.line_chart(df[['A', 'B', 'C']])

with col2:
    st.subheader("Gráfico de Barras")
    st.bar_chart(df[['A', 'B']].abs()) # valores absolutos

# 2. Mapas (st.map)
st.header("2. Mapas Nativos (st.map)")
st.write("Si tu DataFrame tiene columnas 'lat' y 'lon', se mapea automáticamente.")

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [40.4168, -3.7038], # Cerca de Madrid
    columns=['lat', 'lon']
)
st.map(map_data, zoom=10)

# 3. Integración con Plotly (st.plotly_chart)
st.divider()
st.header("3. Gráficos Interactivos Avanzados (Plotly)")

st.info("Para mayor control, interacción y personalización, usa Plotly con st.plotly_chart.")

# Scatter Plot Interactivo con Plotly Express
fig = px.scatter(
    df, x='A', y='B', 
    color='categoria', size='C', 
    hover_data=['fecha'],
    title="Análisis Multivariable Interactivo"
)
st.plotly_chart(fig, use_container_width=True) # use_container_width ajusta al ancho de la columna

# 4. Integración con Altair (st.altair_chart)
st.divider()
st.header("4. Gráficos Declarativos (Altair)")

chart = alt.Chart(df).mark_circle().encode(
    x='A', y='B', color='categoria', tooltip=['A', 'B', 'categoria']
).interactive()

st.altair_chart(chart, use_container_width=True)

# 5. Dashboard Combinado (Ejemplo Final)
st.divider()
st.header("5. Dashboard de Ejemplo Combinado")

selected_cat = st.multiselect("Filtrar Categoría:", ['X', 'Y', 'Z'], default=['X', 'Y'])
filtered_df = df[df['categoria'].isin(selected_cat)]

c1, c2 = st.columns([2, 1])

with c1:
    # Gráfico principal grande
    fig_main = px.line(filtered_df, x='fecha', y=['A', 'B'], title="Evolución Temporal")
    st.plotly_chart(fig_main, use_container_width=True)

with c2:
    # Métricas y resumen lateral
    st.metric("Total Registros", len(filtered_df))
    st.metric("Media Valor A", f"{filtered_df['A'].mean():.2f}")
    
    # Gráfico de pastel pequeño
    pie_fig = px.pie(filtered_df, names='categoria', title="Distribución")
    st.plotly_chart(pie_fig, use_container_width=True)
