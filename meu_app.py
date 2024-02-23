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
            st.link_button("Despacho Instalação", "https://telefonicacorp-my.sharepoint.com/:p:/g/personal/pedro_hmartins_telefonica_com/EUsRE3AMTvJOlHiRTOfRFGQB-yfo3S55Or4V90rw83kgwA")
            st.link_button("Abertura de GAUS","https://telefonicacorp-my.sharepoint.com/:b:/r/personal/pedro_hmartins_telefonica_com/Documents/Abertura%20de%20GAUS.pdf?csf=1&web=1&e=1RQOvK")
            st.link_button("Abertura de Tiquete de Terceiros","https://telefonicacorp-my.sharepoint.com/:b:/r/personal/pedro_hmartins_telefonica_com/Documents/Abertura%20de%20Tiquete%20de%20Terceiros.pdf?csf=1&web=1&e=wW1wCN")
            st.link_button("Acesso Datacenter","https://telefonicacorp-my.sharepoint.com/:w:/r/personal/pedro_hmartins_telefonica_com/Documents/Acesso%20Datacenter.docx?d=w2cc1bcf7a6d94cec9d79b940e94a892e&csf=1&web=1&e=I11G4h")
            st.link_button("Codigos Vivo atualizado","https://telefonicacorp-my.sharepoint.com/:x:/r/personal/pedro_hmartins_telefonica_com/Documents/CODIGOS%20VIVO%20atualizado.xlsx?d=wbcb6f89b5b994601a1aee6d85968db16&csf=1&web=1&e=7leXC9")
            st.link_button("Material - Despacho - EC","https://telefonicacorp-my.sharepoint.com/:w:/r/personal/pedro_hmartins_telefonica_com/Documents/MATERIAL%20PASSO%20A%20PASSO%20-%20DESPACHO%20-%20EC.docx?d=w0c3da1a586474de685c6768e00f16781&csf=1&web=1&e=CbVayz")

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
                st.write(f'##########:')

            if __name__ == '__main__':
                formulario()
    class Ativação_Gpon_Router:
        def __init__(self):
            self.titulo = "Ativação_Gpon_Router"
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

                Fibra_Pri = st.text_input('Fibra_Pri:')

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
    class Ativação_Dslan_V35:
        def __init__(self):
            self.titulo = "Ativação_Dslan_V35"
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

                Modem = st.text_input('Modem:')

                Serial = st.text_input('Serial:')

                Roteador = st.text_input('Roteador:')

                Serie = st.text_input('Serie:')

                Cabo = st.text_input('Cabo:')

                Lateral = st.text_input('Lateral:')

                Pares = st.text_input('Pares:')

                Enlace = st.text_input('Enlace:')

                Ruido = st.text_input('Ruido:')

                Isolação = st.text_input('Isolação:')

                Rvt = st.text_input('Rvt:')

                Observação = st.text_input('Observação:')

                Analista_ESSE = st.text_input('Analista_ESSE:')

                if st.button('Gerar Carimbo'):

                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Modem,Serial,Roteador,Serie,Cabo,Lateral,Pares,Enlace,Ruido,Isolação,Rvt,Observação,Analista_ESSE)
            def exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Modem,Serial,Roteador,Serie,Cabo,Lateral,Pares,Enlace,Ruido,Isolação,Rvt,Observação,Analista_ESSE):

                st.subheader('Respostas:')

                st.write(f'Osx: {Osx}')

                st.write(f'ID_vantive: {ID_vantive}')

                st.write(f'Técnico: {Técnico}')

                st.write(f'Telefone: {Telefone}')

                st.write(f'RE: {RE}')

                st.write(f'Ciente: {Ciente}')

                st.write(f'Tel: {Tel}')

                st.write(f'Modem: {Modem}')

                st.write(f'Serial: {Serial}')

                st.write(f'Roteador: {Roteador}')

                st.write(f'Serie: {Serie}')

                st.write(f'Cabo: {Cabo}')

                st.write(f'Lateral: {Lateral}')

                st.write(f'Pares: {Pares}')

                st.write(f'Enlace: {Enlace}')

                st.write(f'Ruido: {Ruido}')

                st.write(f'Isolação: {Isolação}')

                st.write(f'Rvt: {Rvt}')

                st.write(f'Observação: {Observação}')

                st.write(f'Analista_ESSE: {Analista_ESSE}')

            if __name__ == '__main__':
                formulario()
                
    
    class Ativação_Conversor:
        def __init__(self):
            self.titulo = "Ativação_Conversor"

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
                Equipamento_instalado = st.text_input('Equipamento instalado?')
                Serial = st.text_input('Serial:')
                Testou_X_lite = st.text_input('Testou X_lite?')
                Mantenedor = st.text_input('Mantenedor:')
                Tel_mantenedor = st.text_input('Tel_mantenedor:')
                Observação = st.text_input('Observação:')
                Analista_ESSE = st.text_input('Analista_ESSE:')
        
                if st.button('Gerar Carimbo'):
                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Equipamento_instalado,Serial,Testou_X_lite,Mantenedor,Tel_mantenedor,Observação,Analista_ESSE)
            def exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Equipamento_instalado,Serial,Testou_X_lite,Mantenedor,Tel_mantenedor,Observação,Analista_ESSE):
                st.subheader('Respostas:')
                st.write(f'Osx: {Osx}')
                st.write(f'ID_vantive: {ID_vantive}')
                st.write(f'Técnico: {Técnico}')
                st.write(f'Telefone: {Telefone}')
                st.write(f'RE: {RE}')
                st.write(f'Ciente: {Ciente}')
                st.write(f'Tel: {Tel}')
                st.write(f'Equipamento instalado: {Equipamento_instalado}')
                st.write(f'Serial: {Serial}')
                st.write(f'Testou X_lite? {Testou_X_lite}')
                st.write(f'Mantenedor: {Mantenedor}')
                st.write(f'Tel_mantenedor: {Tel_mantenedor}')
                st.write(f'Observação: {Observação}')
                st.write(f'Analista_ESSE: {Analista_ESSE}')

            if __name__ == '__main__':
                formulario()            
    class Vistoria_Intragov:
        def __init__(self):
            self.titulo = "Vistoria_Intragov"
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

                Gtd_Instalou_Rack = st.text_input('Gtd Instalou Rack?')

                Informar_o_porque_o_rack_não_foi_instalado = st.text_input('Informar o porque o rack não foi instalado:')

                Rack_instalado_é_telefonica_ou_cliente = st.text_input('Rack instalado é telefonica ou cliente?')

                O_espaço_no_rack_é_adequado = st.text_input('O espaço no rack é adequado?')

                O_rack_está_proximo_da_lan_ou_servidor_do_cliente = st.text_input('O rack está proximo da lan ou servidor do cliente?')

                Os_dijuntores_usados_são_compartilhados_ou_exclusivos = st.text_input('Os dijuntores usados são compartilhados ou exclusivos?')

                Os_dijuntores_usados_são_identificados = st.text_input('Os dijuntores usados são identificados?')

                A_energia_elétrica_para_redundancia_é_distinta = st.text_input('A energia elétrica para redundancia é distinta?')

                Voltagem_127_ou_220 = st.text_input('Voltagem 127 ou 220?')

                Possui_aterramento = st.text_input('Possui aterramento?')

                A_rede_interna_foi_executada_ou_existente = st.text_input('A rede interna foi executada ou existente?')

                Qual_tipo_de_cabeamento_ultilizado = st.text_input('Qual tipo de cabeamento ultilizado?')

                Quantos_metros = st.text_input('Quantos metros?')

                Observação = st.text_input('Observação:')

                Analista_ESSE = st.text_input('Analista_ESSE:')

                if st.button('Gerar Carimbo'):

                    st.success('Carimbo Gerado com Sucesso!')
                    exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Gtd_Instalou_Rack,Informar_o_porque_o_rack_não_foi_instalado,Rack_instalado_é_telefonica_ou_cliente,O_espaço_no_rack_é_adequado,O_rack_está_proximo_da_lan_ou_servidor_do_cliente,Os_dijuntores_usados_são_compartilhados_ou_exclusivos,Os_dijuntores_usados_são_identificados,A_energia_elétrica_para_redundancia_é_distinta,Voltagem_127_ou_220,Possui_aterramento,A_rede_interna_foi_executada_ou_existente,Qual_tipo_de_cabeamento_ultilizado,Quantos_metros,Observação,Analista_ESSE)
            def exibir_respostas(Osx,ID_vantive,Técnico,Telefone,RE,Ciente,Tel,Gtd_Instalou_Rack,Informar_o_porque_o_rack_não_foi_instalado,Rack_instalado_é_telefonica_ou_cliente,O_espaço_no_rack_é_adequado,O_rack_está_proximo_da_lan_ou_servidor_do_cliente,Os_dijuntores_usados_são_compartilhados_ou_exclusivos,Os_dijuntores_usados_são_identificados,A_energia_elétrica_para_redundancia_é_distinta,Voltagem_127_ou_220,Possui_aterramento,A_rede_interna_foi_executada_ou_existente,Qual_tipo_de_cabeamento_ultilizado,Quantos_metros,Observação,Analista_ESSE):

                st.subheader('Respostas:')

                st.write(f'Osx: {Osx}')

                st.write(f'ID_vantive: {ID_vantive}')

                st.write(f'Técnico: {Técnico}')

                st.write(f'Telefone: {Telefone}')

                st.write(f'RE: {RE}')

                st.write(f'Ciente: {Ciente}')

                st.write(f'Tel: {Tel}')

                st.write(f'Gtd Instalou Rack? {Gtd_Instalou_Rack}')

                st.write(f'Informar o porque o rack não foi instalado: {Informar_o_porque_o_rack_não_foi_instalado}')

                st.write(f'Rack instalado é telefonica ou cliente? {Rack_instalado_é_telefonica_ou_cliente}')

                st.write(f'O espaço no rack é adequado? {O_espaço_no_rack_é_adequado}')

                st.write(f'O rack está proximo da lan ou servidor do cliente? {O_rack_está_proximo_da_lan_ou_servidor_do_cliente}')

                st.write(f'Os dijuntores usados são compartilhados ou exclusivos? {Os_dijuntores_usados_são_compartilhados_ou_exclusivos}')

                st.write(f'Os dijuntores usados são identificados? {Os_dijuntores_usados_são_identificados}')

                st.write(f'A energia elétrica para redundancia é distinta? {A_energia_elétrica_para_redundancia_é_distinta}')

                st.write(f'Voltagem 127 ou 220? {Voltagem_127_ou_220}')

                st.write(f'Possui aterramento? {Possui_aterramento}')

                st.write(f'A rede interna foi executada ou existente? {A_rede_interna_foi_executada_ou_existente}')

                st.write(f'Qual tipo de cabeamento ultilizado? {Qual_tipo_de_cabeamento_ultilizado}')

                st.write(f'Quantos metros? {Quantos_metros}')

                st.write(f'Observação: {Observação}')

                st.write(f'Analista_ESSE: {Analista_ESSE}')

            if __name__ == '__main__':

                formulario()
                
def main():
        st.sidebar.title("Navegação")
        opcao_pagina = st.sidebar.radio("Escolha um Carimbo", ["Principal","Deslocamento", "Abertura de Horario","Notificação","Baixa_DDR","Ativação_Gpon_Router","Ativação_Dslan_V35","Ativação_SWT_Router","Ativação_Conversor","Vistoria_Intragov"])
           
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
        elif opcao_pagina == "Ativação_Gpon_Router":
            pagina = Ativação_Gpon_Router()
        elif opcao_pagina == "Ativação_Dslan_V35":
            pagina = Ativação_Dslan_V35()
        elif opcao_pagina == "Ativação_SWT_Router":
         pagina = Ativação_SWT_Router()
        elif opcao_pagina == "Ativação_Conversor":
            pagina = Ativação_Conversor()
        elif opcao_pagina == "Vistoria_Intragov":
            pagina = Vistoria_Intragov()

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
else:
    st.error("Credenciais inválidas. Tente novamente.")
    
        
