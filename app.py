import streamlit as st
from middle_squared import run as middle_squared_run
from mcl import run as mcl_run

# Sidebar para seleccionar método
method = st.sidebar.selectbox(
    "Seleccione el método de generación",
    ["Método del Cuadrado Medio", "Método Congruencial Lineal"]
)

# Lógica para cambiar el método
if method == "Método del Cuadrado Medio":
    st.title('Generador de Números Pseudoaleatorios - Método del Cuadrado Medio')
    middle_squared_run()

if method == "Método Congruencial Lineal":
    st.title('Generador de Números Pseudoaleatorios - Método Congruencial Lineal')
    mcl_run()
