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
                Telefone = st.text_input('Telefone:')
                RE = st.text_input('RE:')
                Observação = st.text_input('Observação:')
                Despacho = st.text_input('Despacho:')
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Deslocamento,Técnico,Telefone,RE,Observação,Despacho)
            def exibir_respostas(Deslocamento, Técnico,Telefone,RE,Observação,Despacho):
                st.subheader('Respostas:')
                st.write(f'Deslocamento: {Deslocamento}')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'RE: {RE}')
                st.write(f'Observação: {Observação}')
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
    class Notificação:
        def __init__(self):
            self.titulo = "Notificação"

        def mostrar(self):
            st.title(self.titulo)
            # Adicione mais elementos à sua página inicial conforme necessário
            def formulario():
                Notificação = st.text_input('Notificação:')
                Técnico = st.text_input('Técnico:')
                Telefone = st.text_input('Telefone:')
                RE = st.text_input('RE:')
                Observação = st.text_input('Observação:')
                Despacho = st.text_input('Despacho:')
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Notificação,Técnico,Telefone,RE,Observação,Despacho)
            def exibir_respostas(Notificação, Técnico,Telefone,RE,Observação,Despacho):
                st.subheader('Respostas:')
                st.write(f'Notificação: {Notificação}')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'RE: {RE}')
                st.write(f'Observação: {Observação}')
                st.write(f'Despacho: {Despacho}')
            if __name__ == '__main__':
                 formulario()

    class Baixa_DDR:
        def __init__(self):
            self.titulo = "BAIXA_DDR"

        def mostrar(self):
            st.title(self.titulo)
            # Adicione mais elementos à sua página inicial conforme necessário
            def formulario():
                Técnico = st.text_input('Técnico:')
                Telefone = st.text_input('Telefone:')
                RE = st.text_input('RE:')
                Ciente = st.text_input('Ciente:')
                Tel = st.text_input('Tel:')
                Modem = st.text_input('Modem:')
                Serial = st.text_input('Serial:')
                Testes_certificação = st.text_input('Testes_certificação:')
                Facilidades = st.text_input('Facilidades:')
                Teste_R2 = st.text_input('Teste_R2:')
                Teste_CPA = st.text_input('Teste_CPA:')
                Observação = st.text_input('Observação:')
                Analista_ESSE = st.text_input('Analista_ESSE:')
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Técnico,Telefone,RE,Ciente,Tel,Modem,Serial,Testes_certificação,Facilidades,Teste_R2,Teste_CPA,Observação,Analista_ESSE)
            def exibir_respostas(Técnico,Telefone,RE,Ciente,Tel,Modem,Serial,Testes_certificação,Facilidades,Teste_R2,Teste_CPA,Observação,Analista_ESSE):
                st.subheader('Respostas:')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'RE: {RE}')
                st.write(f'Ciente: {Ciente}')
                st.write(f'Tel: {Tel}')
                st.write(f'Modem: {Modem}')
                st.write(f'Serial: {Serial}')
                st.write(f'Testes_certificação: {Testes_certificação}')
                st.write(f'Facilidades: {Facilidades}')
                st.write(f'Teste_R2: {Teste_R2}')
                st.write(f'Teste_CPA: {Teste_CPA}')
                st.write(f'Observação: {Observação}')
                st.write(f'Analista_ESSE: {Analista_ESSE}')
            if __name__ == '__main__':
                formulario()


    class Ativação_Gpon_e_Router:
        def __init__(self):
            self.titulo = "Ativação_Gpon_e_Router"

        def mostrar(self):
            st.title(self.titulo)
            # Adicione mais elementos à sua página inicial conforme necessário
	def formulario():
		Osx = st.text_input('Osx:')
		ID_vantive = st.text_input('ID_vantive:')
		Técnico = st.text_input('Técnico:')
		Telefone = st.text_input('Telefone:')
		RE = st.text_input('RE:')
		Ciente = st.text_input('Ciente:')
		Tel = st.text_input('Tel:')
		Ont = st.text_input('Ont:')
		Serial = st.text_input('Serial:')
		Roteador = st.text_input('Roteador:')
		Serie = st.text_input('Serie:')
		Facilidades_Gpon = st.text_input('Facilidades_Gpon:')
		Cabo = st.text_input('Cabo:')
		Fibra_Sec = st.text_input('Fibra_Sec:')
		Rvt = st.text_input('Rvt:')
		Observação = st.text_input('Observação:')
		Analista_ESSE = st.text_input('Analista_ESSE:')
		if st.button('Gerar Carimbo'):
			st.success('Carimbo Gerado com Sucesso!')
		                exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Ont,Serial,Roteador,Serie,Facilidades_Gpon,Cabo,Fibra_Pri,Fibra_Sec,Rvt,Observação,Analista_ESSE)
            def exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Ont,Serial,Roteador,Serie,Facilidades_Gpon,Cabo,Fibra_Pri,Fibra_Sec,Rvt,Observação,Analista_ESSE):
                st.subheader('Respostas:')
                st.write(f'Osx: {Osx}')
		st.write(f'ID_vantive: {ID_vantive}')
		st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'RE: {RE}')
                st.write(f'Ciente: {Ciente}')
                st.write(f'Tel: {Tel}')
                st.write(f'Ont: {Ont}')
                st.write(f'Serial: {Serial}')
		st.write(f'Roteador: {Roteador}')
                st.write(f'Serie: {Serie}')
                st.write(f'Facilidades_Gpon: {Facilidades_Gpon}')
		st.write(f'Cabo: {Cabo}')
                st.write(f'Fibra_Pri: {Fibra_Pri}')
                st.write(f'Fibra_Sec: {Fibra_Sec}')
		st.write(f'Rvt: {Rvt}')
                st.write(f'Observação: {Observação}')
                st.write(f'Analista_ESSE: {Analista_ESSE}')
            if __name__ == '__main__':
                formulario()


    def main():
        st.sidebar.title("Navegação")
        opcao_pagina = st.sidebar.radio("Escolha um Carimbo", ["Principal","Deslocamento", "Abertura de Horario","Notificação","Baixa_DDR","Ativação_Gpon_e_Router"])

        if opcao_pagina == "Principal":
            pagina =  Principal()
        elif opcao_pagina == "Deslocamento":
            pagina = Deslocamento()
        elif opcao_pagina == "Abertura de Horario":
            pagina = AberturadeHorario()
        elif opcao_pagina == "Notificação":
            pagina = Notificação()
        elif opcao_pagina == "Baixa_DDR":
            pagina = Baixa_DDR()
        elif opcao_pagina == "Ativação_Gpon_e_Router":
            pagina = Ativação_Gpon_e_Router()

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
