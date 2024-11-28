import streamlit as st
from middle_squared import run as middle_squared_run
from mcl import run as mcl_run
from middle_product import run as middle_product_run
from mcm import run as mcm_run

# Sidebar para seleccionar método
method = st.sidebar.selectbox(
    "Seleccione el método de generación",
    ["Método del Cuadrado Medio", "Método Congruencial Lineal", "Método del Producto Medio","Método Congruencial Multiplicativo"]
)

# Lógica para cambiar el método
if method == "Método del Cuadrado Medio":
    st.title('Generador de Números Pseudoaleatorios - Método del Cuadrado Medio')
    middle_squared_run()

if method == "Método Congruencial Lineal":
    st.title('Generador de Números Pseudoaleatorios - Método Congruencial Lineal')
    mcl_run()

if method == "Método del Producto Medio":
    st.title('Generador de Números Pseudoaleatorios - Método del Producto Medio')
    middle_product_run()

if method == "Método Congruencial Multiplicativo":
    st.title('Generador de Números Pseudoaleatorios - Método Congruencial Multiplicativo')
    mcm_run()
