import streamlit as st

def middle_squared_method(seed1, n):
    results = []
    for _ in range(n):
        squared = seed1 ** 2
        len_squared = len(str(squared))
        len_seed = len(str(seed1))
        start = (len_squared - len_seed) // 2
        seed1 = int(str(squared)[int(start):int(start) + len_seed])
        results.append(seed1)
    return results

def run():
    st.subheader('Configuración para el Método del Cuadrado Medio')

    seed1 = st.number_input(
        'Ingrese la semilla (3 o más dígitos):',
        min_value=100,
        step=1,
        key="middle_squared_seed"
    )
    n = st.number_input(
        'Ingrese la cantidad de números a generar:',
        min_value=1,
        step=1,
        key="middle_squared_n"
    )

    if st.button('Generar', key="middle_squared_button"):
        if len(str(seed1)) >= 3:
            results = middle_squared_method(seed1, n)
            st.write('Números Pseudoaleatorios Generados:')
            st.write(results)
        else:
            st.error('La semilla debe tener 3 o más dígitos.')
