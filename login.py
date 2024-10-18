import streamlit as st
import pandas as pd
import requests


hostname = '127.0.0.1:8000'

def validarUsuario(usuario,clave):
    """Permite la validación de usuario y clave

    Args:
        usuario (str): usuario a validar
        clave (str): clave del usuario

    Returns:
        bool: True usuario valido, False usuario invalido
    """
    content = requests.get(f'http://{hostname}/remision/user/{usuario}')
    if content.content == b'null':
        return False
    else:
        content = content.json()
        if content['password'] == clave:
            list_user = pd.read_csv('usuarios.csv')
            data = {'usuario': [usuario]}
            list_user = pd.concat([list_user, pd.DataFrame(data)], axis=0)
            list_user = list_user.drop_duplicates()
            list_user.to_csv('usuarios.csv', index=False)
            return True


def generarMenu(usuario):
    """Genera el menú dependiendo del usuario

    Args:
        usuario (str): usuario utilizado para generar el menú
    """
    with st.sidebar:
        # Cargamos la tabla de usuarios
        dfusuarios = pd.read_csv('usuarios.csv')
        # Filtramos la tabla de usuarios
        dfUsuario =dfusuarios[(dfusuarios['usuario']==usuario)]
        # Cargamos el nombre del usuario

        #Mostramos el nombre del usuario
        # st.write(f"Hola **:blue-background[{nombre}]** ")
        # Mostramos los enlaces de páginas
        st.page_link("inicio.py", label="Inicio", icon=":material/home:")
        # st.subheader("Tableros")
        # st.page_link("pages/remision.py", label="Busqueda remision", icon=":material/search:")
        # st.page_link("pages/pagina2.py", label="Compras", icon=":material/shopping_cart:")
        # st.page_link("pages/pagina3.py", label="Personal", icon=":material/group:")
        # Botón para cerrar la sesión
        btnSalir=st.button("Salir")
        if btnSalir:
            st.session_state.clear()
            # Luego de borrar el Session State reiniciamos la app para mostrar la opción de usuario y clave
            st.rerun()

def generarLogin():
    """Genera la ventana de login o muestra el menú si el login es valido
    """
    # Validamos si el usuario ya fue ingresado
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario']) # Si ya hay usuario cargamos el menu
    else:
        # Cargamos el formulario de login
        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuario')
            parPassword = st.text_input('Password',type='password')
            btnLogin=st.form_submit_button('Ingresar',type='primary')
            if btnLogin:
                if validarUsuario(parUsuario,parPassword):
                    st.session_state['usuario'] =parUsuario
                    # Si el usuario es correcto reiniciamos la app para que se cargue el menú
                    st.rerun()
                else:
                    # Si el usuario es invalido, mostramos el mensaje de error
                    st.error("Usuario o clave inválidos",icon=":material/gpp_maybe:")