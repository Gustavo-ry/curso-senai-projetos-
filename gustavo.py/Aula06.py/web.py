import streamlit as  st
import pandas as pd

dados = {}
Nome = st.text_input('Digite seu nome:')
idade = (st.number_input('Digite sua idade:', min_value=0, step=1))
cadastrar = st.button('cadastrar')


if 'dados' not in st.session_state:
    st.session_state.dados = pd.DataFrame({
    'Nome': ['Ana', 'João', 'Maria'],
    'idade': [25, 30, 22],
})



if cadastrar :
    if Nome:
        novo= pd.DataFrame({'Nome': [Nome], 'idade': [idade]})
        st.session_state.dados = pd.concat(
            [st.session_state.dados, novo],
            ignore_index=True
        )
        st.success('Adicionado!')
        st.balloons()
        st.snow()                    
    
else:
    st.warning('Por favor, digite um nome.')



st.dataframe(st.session_state.dados)

