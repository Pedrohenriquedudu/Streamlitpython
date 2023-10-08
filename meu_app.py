import streamlit as st
import pandas as pd

st.set_page_config(page_title="SITE APOIO GTD DADOS B2B")

with st.container():
    st.title("Suporte a campo SPI Dados B2B")
    st.markdown(''' 
Formulários para gerar Scripts:
''')   
    st.link_button("SWT DATACOM DM-2104", "https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
    st.link_button("ROTEADORES B2B", "https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
    st.link_button("CONVERSORES", "https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
