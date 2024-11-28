import streamlit as st

def multiplicative_congruential_method(seed, a, m, n):
    results = []
    for _ in range(n):
        seed = (a * seed) % m
        results.append(seed)
    return results

def run():
    st.subheader('Configuración para el Método Congruencial Multiplicativo')

    seed = st.number_input(
        'Ingrese la semilla:',
        min_value=0,
        step=1,
        key="mcg_seed"
    )
    a = st.number_input(
        'Ingrese el multiplicador (a):',
        min_value=1,
        step=1,
        key="mcg_a"
    )
    m = st.number_input(
        'Ingrese el módulo (m):',
        min_value=1,
        step=1,
        key="mcg_m"
    )
    n = st.number_input(
        'Ingrese la cantidad de números a generar:',
        min_value=1,
        step=1,
        key="mcg_n"
    )

    if st.button('Generar', key="mcg_button"):
        results = multiplicative_congruential_method(seed, a, m, n)
        st.write('Números Pseudoaleatorios Generados:')
        st.write(results)

if __name__ == "__main__":
    run()
