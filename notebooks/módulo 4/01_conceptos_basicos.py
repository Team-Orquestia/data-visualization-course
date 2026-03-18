import streamlit as st
import pandas as pd


# 1. Configuración de la página (siempre al principio)
st.set_page_config(
    page_title="Mi Primera App de Datos",
    page_icon="📊",
    layout="centered"
)

# 2. Textos y Títulos
st.title("Bienvenido al curso de Streamlit")
st.header("Conceptos Básicos")
st.write("""
Streamlit es una librería de Python que te permite convertir scripts de datos en aplicaciones web compartibles en minutos.
Todo el código se ejecuta de arriba a abajo cada vez que el usuario interactúa con la aplicación.
""")

# 3. Mostrar Datos (Dataframes)
st.subheader("Visualización de Tablas")

# Creamos un dataset de ejemplo
df = pd.DataFrame({
    'Nombre': ['Ana', 'Carlos', 'Elena', 'David'],
    'Edad': [25, 30, 22, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Puntuación': [88, 92, 79, 85]
})

# st.dataframe permite scroll y ordenación
st.write("Uso de st.dataframe (interactivo):")
st.dataframe(df)

# st.table es estático (todo el contenido visible)
st.write("Uso de st.table (estático):")
st.table(df)

# 4. Métricas
st.subheader("Métricas KPI")
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "24 °C", "1.2 °C")
col2.metric("Viento", "9 km/h", "-8%")
col3.metric("Humedad", "86%", "4%")

# 5. Código y JSON
st.subheader("Otros elementos")
st.code("print('Hola Streamlit')", language='python')
st.json({'foo': 'bar', 'baz': 'boz'})
