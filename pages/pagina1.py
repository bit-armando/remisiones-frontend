import streamlit as st
import login
from remision import remision

login.generarLogin()
if 'usuario' in st.session_state:
    remision()
    # st.header('Página :blue[1]')