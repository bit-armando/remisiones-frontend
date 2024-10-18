import streamlit as st
import login as login
import webbrowser
from utils.texto import guion

st.header('Página :orange[remisiones]')
login.generarLogin()
if 'usuario' in st.session_state:
    with st.form('frmLogin'):
        hostname = '127.0.0.1:8000'
        st.title('Busqueda de remisiones')
        num_remison = st.text_input('No. Remision')
        btnBuscar = st.form_submit_button('Buscar', type='primary')

        if btnBuscar:
            st.link_button('Ver documento', f"http://{hostname}/remision/ver/{guion(num_remison)}")
            # webbrowser.open_new_tab(f"http://{hostname}/remision/ver/{guion(num_remison)}")