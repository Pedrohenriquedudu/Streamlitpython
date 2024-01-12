import streamlit as st
import pandas as pd
import time
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

    class Principal:
        def __init__(self):
            self.titulo = "Instrução de Trabalho ESSE B2B :book:"
            
           
        def mostrar(self):
            st.title(self.titulo)

            with st.container():
                 
                 st.markdown(''' 
CONSULTAS: :point_down:
''') 
            st.link_button("Desp. Instalação", "https://drive.google.com/file/d/1utRUjjDKYST3wYd6E5BaD3XKYysge29T/view?usp=sharing")
            st.link_button("Codigos Remedy","https://docs.google.com/document/d/1pUbdXcrXbND1yGss9p3s9uLjctUPSPy5/edit?usp=sharing&ouid=115435742445522021005&rtpof=true&sd=true")
           

    class Deslocamento:
        def __init__(self):
            self.titulo = "Deslocamento"

        def mostrar(self):
            st.title(self.titulo)
            # Adicione mais elementos à sua página inicial conforme necessário
            def formulario():
                Deslocamento = st.text_input('Deslocamento:')
                Técnico = st.text_input('Técnico:')
                Despacho = st.text_input('Despacho:')
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Deslocamento,Técnico, Despacho)
            def exibir_respostas(Deslocamento, Técnico, Despacho):
                st.subheader('Respostas:')
                st.write(f'Deslocamento: {Deslocamento}')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Despacho: {Despacho}')
            if __name__ == '__main__':
                formulario()

    class AberturadeHorario:
        def __init__(self):
            self.titulo = "Abertura de Horario"

        def mostrar(self):
            st.title(self.titulo)
            def formulario():
                Técnico = st.text_input('Técnico:')
                Telefone= st.text_input('Telefone:')
                Ciente= st.text_input('Ciente:')
                Tel= st.text_input('Tel:')
                Observação= st.text_input('Observação:')
                Despacho = st.text_input('Despacho:')
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Técnico,Telefone,Ciente,Tel,Observação,Despacho)
            def exibir_respostas(Técnico,Telefone,Ciente,Tel,Observação,Despacho):
                st.subheader('Respostas:')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'Ciente: {Ciente}')
                st.write(f'Tel: {Tel}')
                st.write(f'Observação: {Observação}')
                st.write(f'Despacho: {Despacho}')
            if __name__ == '__main__':
                formulario()
            # Adicione mais elementos à sua página secundária conforme necessário

    def main():
        st.sidebar.title("Navegação")
        opcao_pagina = st.sidebar.radio("Escolha um Carimbo", ["Principal","Deslocamento", "Abertura de Horario"])

        if opcao_pagina == "Principal":
            pagina =  Principal()
        elif opcao_pagina == "Deslocamento":
            pagina = Deslocamento()
        elif opcao_pagina == "Abertura de Horario":
            pagina = AberturadeHorario()

        pagina.mostrar()

    if __name__ == "__main__":
        main()

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

