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
def resolver_ecuacion(m, n, p):
    if m != 0:
        return m/p-n/p
    else:
        return None

# Título de la aplicación
st.title("Generador y Solucionador de Ecuaciones de 1º")

# Botón para generar una nueva ecuación
st.button("Generar Ecuación: Ax+B=C")
a, b, c = generar_ecuacion()
st.write(f"La ecuación generada es: {a}x + {b} = {c}")

valorA = st.text_input("Valor de A:", a)
valorB = st.text_input("Valor de B:", b)
valorC = st.text_input("Valor de C:", c)

st.markdown(f"Solución de {valorA}x+{valorB}={valorC}")
solucion = resolver_ecuacion(valorA, valorB, valorC)
st.write(solucion)
