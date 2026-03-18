import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Layouts Avanzados con Streamlit")

# 1. Sidebar (Barra Lateral)
# Usar `with st.sidebar` es la forma más pythonica
with st.sidebar:
    st.header("1. Barra Lateral")
    st.write("Coloca widgets de navegación y configuración aquí.")
    modo_oscuro = st.toggle("Activar modo oscuro (simulado)")
    
    # 2. Tabs en Sidebar
    tab1_s, tab2_s = st.tabs(["Filtros", "General"])
    with tab1_s:
        region = st.selectbox("Región", ["Norte", "Sur", "Este", "Oeste"])
    with tab2_s:
        st.write("Versión 1.0.0")

# 3. Columnas Principales
st.divider()
st.header("2. División en Columnas (st.columns)")

col_izq, col_centro, col_der = st.columns([1, 2, 1]) # Proporciones de ancho

with col_izq:
    st.image("https://Placehold.co/150", caption="Logo Empresa")
    st.info("Columna Izquierda (Ancho: 1)")

with col_centro:
    st.warning("Columna Central (Ancho: 2)")
    # Gráfico simple
    data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(data)

with col_der:
    st.success("Columna Derecha (Ancho: 1)")
    st.metric(label="Visitas", value="160K", delta="1.2%")

# 4. Pestañas (st.tabs)
st.divider()
st.header("3. Pestañas de Contenido (st.tabs)")

tab1, tab2, tab3 = st.tabs(["📈 Analítica", "📄 Datos", "ℹ️ Información"])

with tab1:
    st.subheader("Dashboard Analítico")
    # Dos columnas dentro de una pestaña
    c1, c2 = st.columns(2)
    c1.bar_chart(data)
    c2.scatter_chart(data)

with tab2:
    st.subheader("Visualización de Datos Crudos")
    st.dataframe(data)

with tab3:
    st.subheader("Acerca de este proyecto")
    st.markdown("""
    Esta sección utiliza pestañas para organizar el contenido.
    - **Pestaña 1:** Gráficos interactivos
    - **Pestaña 2:** Tabla de datos
    - **Pestaña 3:** Documentación
    """)

# 5. Expander (st.expander)
st.divider()
st.header("4. Contenido Plegable (st.expander)")

with st.expander("Ver código fuente de la configuración"):
    st.code("""
    st.set_page_config(layout="wide")
    col1, col2 = st.columns(2)
    """, language="python")

with st.expander("Detalles técnicos avanzados", expanded=False):
    st.json({
        "status": "ok",
        "latency": "25ms",
        "server": "us-east-1"
    })

# 6. Container (st.container)
st.divider()
st.header("5. Contenedores Dinámicos (st.container)")
st.write("Útil para insertar elementos fuera de orden o agrupar lógica.")

contenedor_principal = st.container()
contenedor_principal.write("Esto está dentro de un contenedor.")

# Puedes escribir en el contenedor más tarde desde cualquier parte del código
if st.button("Añadir mensaje al contenedor de arriba"):
    contenedor_principal.success("¡Mensaje insertado dinámicamente desde abajo!")
