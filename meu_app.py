import streamlit as st
import pandas as pd

st.set_page_config(page_title="SITE APOIO GTD DADOS B2B")

with st.container():
    st.title("Suporte a campo SPI Dados B2B")
    st.markdown(''' 
Formulários para gerar Scripts:
''')   
    st.link_button("SWT DATACOM DM-2104", "https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
    st.link_button("ROTEADORES B2B", "https://colab.research.google.com/drive/1XXxemoXIcGC72XSWdW4pZd5AtgZYSx-H?usp=sharing")
    st.link_button("CONVERSORES_SIP_TDM", "https://colab.research.google.com/drive/12yVdAx7O-g5K4H_UY5_RApN4o2AIzZ-F?usp=sharing")
with st.container():
    st.markdown(''' 
Repositorios IOS >>>
''') 
    binary_contents = b'c1100-universalk9_ias.16.09.06.SPA.bin'
# Defaults to 'application/octet-stream'
st.download_button('Download c1100-universalk9_ias.16.09.06.SPA.bin', binary_contents)
