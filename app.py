import streamlit as st
import random

# Función para generar una ecuación de primer grado
def generar_ecuacion():
    # Generar coeficientes aleatorios para la ecuación ax + b = 0
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    return a, b

# Función para resolver la ecuación ax + b = 0
def resolver_ecuacion(a, b):
    if a != 0:
        return -b / a
    else:
        return None

# Título de la aplicación
st.title("Generador y Solucionador de Ecuaciones de 1º")

# Botón para generar una nueva ecuación
if st.button("Generar Ecuación: Ax+B=0"):
    a, b = generar_ecuacion()
    st.write(f"La ecuación generada es: {a}x + {b} = 0")

# Botón para generar una nueva ecuación
if st.button(f"Solución de: {a}x + {b} = 0"):
    # Resolver la ecuación
    valorA = st.text_input("Escribe el valor de A: ","A")
    valorB = st.text_input("Escribe el valor de B: ","B")
    
    solucion = resolver_ecuacion(a, b)
    if solucion is not None:
        st.write(f"La solución es: x = {solucion}")
    else:
        st.write("La ecuación no tiene solución, ya que a = 0.")
