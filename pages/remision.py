import streamlit as st
import requests

from utils.texto import guion

hostname = '127.0.0.1:8000'

def login():
    st.title('Login')
    user = st.text_input('Usuario')
    password = st.text_input('Contraseña')
    button = st.button('ENTRAR')

    if button:
        content = requests.get(f'http://{hostname}/remision/user/{user}')
        if content.content == b'null':
            st.error('Usuario y/o contraseña incorrectos')
        else:
            content = content.json()
            if content['password'] == password:
                return True


def remision():
    st.title('Busqueda de remisiones')
    num_remison = st.text_input('No. Remision')
    st.link_button('Consultar',f"http://{hostname}/remision/ver/{guion(num_remison)}")

