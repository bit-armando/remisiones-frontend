import streamlit as st

from utils.texto import guion

st.title('Busqueda de remisiones')
num_remison = st.text_input('No. Remision')

st.link_button('Consultar',f"http://10.236.21.166:8000/remision/ver/{guion(num_remison)}")