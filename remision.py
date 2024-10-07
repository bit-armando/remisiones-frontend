import streamlit as st

from utils.texto import guion

st.title('Busqueda de remisiones')
num_remison = st.text_input('No. Remision')

st.link_button('Consultar',f"http://127.0.0.1:8000/remision/ver/{guion(num_remison)}")