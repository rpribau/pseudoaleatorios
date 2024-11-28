import streamlit as st

def linear_congruential_method(seed, a, c, m, n):
    results = []
    for _ in range(n):
        seed = (a * seed + c) % m
        results.append(seed)
    return results

def run():
    st.subheader('Configuración para el Método Congruencial Lineal')

    seed = st.number_input(
        'Ingrese la semilla:',
        min_value=0,
        step=1,
        key="lcg_seed"
    )
    a = st.number_input(
        'Ingrese el multiplicador (a):',
        min_value=1,
        step=1,
        key="lcg_a"
    )
    c = st.number_input(
        'Ingrese el incremento (c):',
        min_value=0,
        step=1,
        key="lcg_c"
    )
    m = st.number_input(
        'Ingrese el módulo (m):',
        min_value=1,
        step=1,
        key="lcg_m"
    )
    n = st.number_input(
        'Ingrese la cantidad de números a generar:',
        min_value=1,
        step=1,
        key="lcg_n"
    )

    if st.button('Generar', key="lcg_button"):
        results = linear_congruential_method(seed, a, c, m, n)
        st.write('Números Pseudoaleatorios Generados:')
        st.write(results)

if __name__ == "__main__":
    run()
