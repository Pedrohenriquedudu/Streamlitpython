import streamlit as st
import pandas as pd

with st.container():
    st.title("Suporte a campo SPI Dados B2B :sunglasses:")
    st.markdown(''' 
Formulários para gerar Scripts:
''')   
    st.link_button("SWT DATACOM DM-2104", "https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
    st.link_button("ROTEADORES B2B", "https://colab.research.google.com/drive/1XXxemoXIcGC72XSWdW4pZd5AtgZYSx-H?usp=sharing")
    st.link_button("CONVERSORES_SIP_TDM", "https://colab.research.google.com/drive/12yVdAx7O-g5K4H_UY5_RApN4o2AIzZ-F?usp=sharing")
with st.container():
    st.markdown(''' 
Firmware e IOS: :point_down:
''') 
st.link_button("Repositórios IOS","https://drive.google.com/drive/folders/1lU9-1yEFGuEQIt5FtHuAM9VQjJXhhERY?usp=sharing")

with st.sidebar:
    
    st.write("Materiais para Downloads")

    with st.spinner("Loading..."):
        time.sleep(3)
        st.link_button("Downloads", "https://drive.google.com/drive/folders/1dvHJka8s_3Pdtzif6ZLEgrG4pWBB46qn?usp=sharing")
