import streamlit as st

st.title("Gestión de Estado (Session State) y Callbacks")
st.write("""
Por defecto, Streamlit recarga todo el script cada vez que interactúas con un widget. 
Esto significa que las variables se reinician. 
Para mantener información entre recargas (como un contador, una lista de tareas, o un carrito de compras), usamos `st.session_state`.
""")

# 1. Ejemplo Básico: El Contador Persistente
st.header("1. El Problema del Estado")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sin Session State")
    count = 0
    if st.button("Incrementar (Reset)"):
        count += 1
    st.write(f"Conteo: {count}")
    st.caption("Siempre vuelve a 0 porque `count` se reinicializa en cada ejecución.")

with col2:
    st.subheader("Con Session State")
    # Inicializar la variable en session_state si no existe
    if 'my_counter' not in st.session_state:
        st.session_state.my_counter = 0

    if st.button("Incrementar (Persistente)"):
        st.session_state.my_counter += 1
    st.write(f"Conteo: {st.session_state.my_counter}")
    st.caption("Mantiene el valor entre ejecuciones.")


# 2. Callbacks
st.markdown("---")
st.header("2. Callbacks y on_change")

st.write("Podemos ejecutar funciones específicas cuando un widget cambia su valor, usando `on_change` o `on_click`.")

def clear_text():
    # Esta función se ejecuta antes de que el resto del script se recargue
    st.session_state.my_text_input = ""
    st.session_state.last_message = "¡Texto borrado mediante callback!"

if 'last_message' not in st.session_state:
    st.session_state.last_message = ""

# Input vinculado a session_state mediante 'key'
text = st.text_input(
    "Escribe algo y presiona Enter:", 
    key="my_text_input" # 'key' crea automáticamente st.session_state.my_text_input
)

st.write(f"Texto actual: {text}")

# Botón que llama a la función `clear_text`
st.button("Borrar Texto (Callback)", on_click=clear_text)

if st.session_state.last_message:
    st.success(st.session_state.last_message)


# 3. Aplicación Práctica: Lista de Tareas (To-Do List)
st.markdown("---")
st.header("3. Ejemplo Práctico: Lista de Tareas")

# Inicializar lista de tareas
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Input para nueva tarea
new_task = st.text_input("Nueva Tarea:", key="new_task_input")

def add_task():
    task_text = st.session_state.new_task_input
    if task_text:
        st.session_state.tasks.append({"name": task_text, "done": False})
        # Limpiar el input manualmente seria complejo sin session_state, 
        # pero aquí podríamos resetearlo si quisiéramos, aunque streamlit lo maneja bien.
        st.session_state.new_task_input = "" # Limpiar input

st.button("Añadir Tarea", on_click=add_task)

st.subheader("Mis Tareas")

# Iterar y mostrar tareas
# Nota: Modificar una lista mientras se itera puede ser tricky, aquí lo hacemos simple
for i, task in enumerate(st.session_state.tasks):
    col_a, col_b = st.columns([0.1, 0.9])
    
    with col_a:
        # Checkbox vinculado al estado de la tarea
        # Usamos una key única para cada checkbox basada en el índice
        is_done = st.checkbox(
            "Hecho", 
            key=f"check_{i}",
            value=task["done"]
        )
        # Actualizar estado
        st.session_state.tasks[i]["done"] = is_done
    
    with col_b:
        if task["done"]:
            st.markdown(f"~~{task['name']}~~")
        else:
            st.write(task["name"])

# Botón para limpiar completadas
if st.button("Eliminar tareas completadas"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.rerun() # Recargar la app para reflejar cambios inmediatamente

# Debugging State
with st.expander("Ver estado completo de la sesión"):
    st.write(st.session_state)
