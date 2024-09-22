import streamlit as st
import random

# Inicializar variables en la sesión
if 'a' not in st.session_state:
    st.session_state['a'] = None
if 'b' not in st.session_state:
    st.session_state['b'] = None

# Función para generar una ecuación de primer grado
def generar_ecuacion():
    # Generar coeficientes aleatorios para la ecuación ax + b = 0
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    st.session_state['a'] = a
    st.session_state['b'] = b

# Función para resolver la ecuación ax + b = 0
def resolver_ecuacion(a, b):
    if a != 0:
        return -b / a
    else:
        return None

# Título de la aplicación
st.title("Generador y Solucionador de Ecuaciones de Primer Grado")

# Botón para generar una nueva ecuación
if st.button("Generar Ecuación"):
    generar_ecuacion()
    st.write(f"La ecuación generada es: {st.session_state['a']}x + {st.session_state['b']} = 0")

# Botón para mostrar la solución
if st.button("Mostrar Solución"):
    a = st.session_state['a']
    b = st.session_state['b']
    if a is not None and b is not None:
        st.write(f"La ecuación actual es: {a}x + {b} = 0")
        solucion = resolver_ecuacion(a, b)
        if solucion is not None:
            st.write(f"La solución es: x = {solucion}")
        else:
            st.write("La ecuación no tiene solución, ya que a = 0.")
    else:
        st.write("Primero genera una ecuación.")
