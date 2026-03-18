import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title("Interacción con Widgets")
st.write("""
Los widgets son la forma principal de interacción del usuario con la app.
En Streamlit, los widgets se declaran y asignan directamente a variables, sin necesidad de callbacks complejos.
Cada interacción recarga el script completo de arriba a abajo.
""")

# 1. Widgets de Entrada Básicos
st.header("Entradas de Usuario")
nombre = st.text_input("Ingresa tu nombre:")
edad = st.number_input("Ingresa tu edad:", min_value=0, max_value=120)
fecha = st.date_input("Fecha de nacimiento:")
hora = st.time_input("Hora de nacimiento:")

# 2. Selección de Opciones
nivel = st.selectbox(
    "Nivel de experiencia:",
    ("Principiante", "Intermedio", "Avanzado")
)

# 3. Checkboxes y Radio Buttons
if st.checkbox("Mostrar información adicional"):
    st.info("Este es un mensaje informativo que solo aparece si marcas el checkbox.")

genero = st.radio(
    "Género:",
    ("Masculino", "Femenino", "Prefiero no decir")
)

# 4. Sliders y Selección Múltiple
experiencia = st.slider("Años de experiencia:", 0, 50, 5)
idiomas = st.multiselect(
    "Idiomas que hablas:",
    ["Español", "Inglés", "Francés", "Alemán", "Italiano"],
    ["Español"]
)

# 5. Botones y Acciones
if st.button("Procesar Formulario"):
    st.success(f"Formulario enviado por {nombre} ({edad} años). Experiencia: {nivel}")
    st.write("Idiomas seleccionados:", idiomas)

# ----------------------------------------------------------------------------------
# Ejemplo Práctico: Filtrado de Datos
st.markdown("---") # Reemplazo de st.divider() para compatibilidad
st.header("Ejemplo Práctico: Filtrado de Datos en Tiempo Real")

# Crear datos de empleados ficticios
np.random.seed(42)  # Para reproducibilidad
n_empleados = 20
data = pd.DataFrame({
    'ID': range(1, n_empleados + 1),
    'Departamento': np.random.choice(['Ventas', 'IT', 'Marketing', 'RRHH'], n_empleados),
    'Salario': np.random.randint(30000, 90000, n_empleados),
    'Antigüedad': np.random.randint(1, 15, n_empleados),
    'Satisfacción': np.random.uniform(1, 10, n_empleados).round(1)
})

# Filtros
col1, col2 = st.columns(2)
with col1:
    dept_filtro = st.multiselect(
        "Filtrar por departamento:",
        options=data['Departamento'].unique(),
        default=data['Departamento'].unique()
    )
with col2:
    salario_min, salario_max = st.slider(
        "Rango de salario:",
        int(data['Salario'].min()), int(data['Salario'].max()), 
        (int(data['Salario'].min()), int(data['Salario'].max()))
    )

# Aplicar filtros
df_filtrado = data[
    (data['Departamento'].isin(dept_filtro)) &
    (data['Salario'] >= salario_min) &
    (data['Salario'] <= salario_max)
]

st.subheader(f"Resultados ({len(df_filtrado)} empleados encontrados)")
# Convertir a objetos Python antes de estilizar para evitar problemas de compatibilidad
# con el serializador de Streamlit (Arrow) y Pandas 3.0+
st.dataframe(
    df_filtrado.astype(object).style.format({'Salario': '${:,.2f}'}),
    use_container_width=True
)
