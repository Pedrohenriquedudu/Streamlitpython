import streamlit as st
import pandas as pd
import time 
# Defina as credenciais de login
credenciais = {
    "ESSE_SPI": "suporte",
}

# Função de login
def login():
    st.subheader("Despacho B2B SPI :book:")
    username = st.text_input("Nome de usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Login"):
        if username in credenciais and credenciais[username] == senha:
            return True
        else:
            st.error("Credenciais inválidas. Tente novamente.")
    return False

# Página protegida
def pagina_protegida():
    st.title("Carimbos B2B SPI > EC/PE/ARKÉ :desktop_computer:")
    
    st.markdown(''' 
Formulários para gerar CARIMBOS:
''')   
    st.link_button("CARIMBO PE","https://colab.research.google.com/drive/1b8AYzFMYrDKcXX51VAtxUe_hHeVmlRK_?usp=sharing")
    st.link_button("CARIMBO EC", "https://colab.research.google.com/drive/1b8AYzFMYrDKcXX51VAtxUe_hHeVmlRK_?usp=sharing")
    st.link_button("CARIMBO ARKÉ","https://colab.research.google.com/drive/1b8AYzFMYrDKcXX51VAtxUe_hHeVmlRK_?usp=sharing")
    with st.container():
                 st.markdown(''' 
CONSULTA CODIGOS: :point_down:
''') 
    st.link_button("CODIGOS REMEDY","https://docs.google.com/document/d/1pUbdXcrXbND1yGss9p3s9uLjctUPSPy5/edit?usp=sharing&ouid=115435742445522021005&rtpof=true&sd=true")

# Confwith st.sidebar:
    with st.sidebar:
    
        st.write("Instrução de Trabalho ESSE :book:")
        with st.spinner("Loading..."):
            time.sleep(3)
        st.link_button("Downloads", "https://drive.google.com/file/d/1utRUjjDKYST3wYd6E5BaD3XKYysge29T/view?usp=sharing")

# Verifique o estado de autenticação
is_authenticated = False

if "is_authenticated" in st.session_state:
    is_authenticated = st.session_state.is_authenticated

# Se o usuário está autenticado, mostre a página protegida
if is_authenticated:
    pagina_protegida()
else:
    is_authenticated = login()
    if is_authenticated:
        st.session_state.is_authenticated = True
        # Redirecione para a página protegida alterando os parâmetros da URL
        st.experimental_set_query_params(authenticated="true")
        st.write("Bem-vindo, " + username)
    else:
        st.error("Credenciais inválidas. Tente novamente.")
        # Adicione aqui o código para a parte protegida da página após o login
