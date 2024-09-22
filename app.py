import streamlit as st
import random

# Función para generar una ecuación de primer grado
def generar_ecuacion():
    # Generar coeficientes aleatorios para la ecuación ax + b = 0
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c

# Función para resolver la ecuación ax + b = 0
def resolver_ecuacion(a, b, c):
    if a != 0:
        return c/a-b/a
    else:
        return None

# Título de la aplicación
st.title("Generador y Solucionador de Ecuaciones de 1º")

# Botón para generar una nueva ecuación
st.button("Generar Ecuación: Ax+B=C")
a, b, c = generar_ecuacion()
st.write(f"La ecuación generada es: {a}x + {b} = {c}")

valorA = st.text_input("Escribe el valor de A:", " ")
valorB = st.text_input("Escribe el valor de B:", " ")
valorC = st.text_input("Escribe el valor de C:", " ")

st.markdown("Solución de Ax+B=C")
solucion = resolver_ecuacion(valorA, valorB, valorC)
st.text(solucion)
