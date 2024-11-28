import streamlit as st

def middle_product_method(seed1, seed2, n):
    results = []
    for _ in range(n):
        product = seed1 * seed2
        len_product = len(str(product))
        len_seed = len(str(seed1))
        start = (len_product - len_seed) // 2
        seed1 = int(str(product)[int(start):int(start) + len_seed])
        results.append(seed1)
        # Actualizar las semillas para la próxima iteración
        seed2 = seed1
    return results

def run():
    st.subheader('Configuración para el Método del Producto Medio')

    seed1 = st.number_input(
        'Ingrese la primera semilla (3 o más dígitos):',
        min_value=100,
        step=1,
        key="middle_product_seed1"
    )
    seed2 = st.number_input(
        'Ingrese la segunda semilla (3 o más dígitos):',
        min_value=100,
        step=1,
        key="middle_product_seed2"
    )
    n = st.number_input(
        'Ingrese la cantidad de números a generar:',
        min_value=1,
        step=1,
        key="middle_product_n"
    )

    if st.button('Generar', key="middle_product_button"):
        if len(str(seed1)) >= 3 and len(str(seed2)) >= 3:
            results = middle_product_method(seed1, seed2, n)
            st.write('Números Pseudoaleatorios Generados:')
            st.write(results)
        else:
            st.error('Ambas semillas deben tener 3 o más dígitos.')

if __name__ == "__main__":
    run()
