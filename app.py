import streamlit as st

def middle_squared_method(seed1, n):
    results = []
    for _ in range(n):
        # Sacar R(n)^2
        squared = seed1 ** 2

        # Verificar longitud de M.R(n)^2 y sacar posición inicial
        len_squared = len(str(squared))
        len_seed = len(str(seed1))
        start = (len_squared - len_seed) / 2

        # Obtener nuevo número pseudoaleatorio
        # Si el valor es de .5, hay dos opciones de numeros pseudoaleatorios
        if len_squared % 2 == 0:
            seed1 = int(str(squared)[int(start):int(start) + len_seed])
        else:
            seed1 = int(str(squared)[int(start) - 1:int(start) + len_seed - 1])

        results.append(seed1)

    return results

st.title('Generador de Números Pseudoaleatorios - Método del Cuadrado Medio')

seed1 = st.number_input('Ingrese la primera semilla (3 o más dígitos):', min_value=100, step=1)
n = st.number_input('Ingrese la cantidad de números a generar:', min_value=1, step=1)

if st.button('Generar'):
    if len(str(seed1)) >= 3:
        results = middle_squared_method(seed1, n)
        st.write('Números Pseudoaleatorios Generados:')
        st.write(results)
    else:
        st.error('Las semillas deben ser números de 3 o más dígitos.')