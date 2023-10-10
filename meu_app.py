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
    data_df = pd.DataFrame(
    {
        "apps": [
            "https://drive.google.com/drive/folders/1lU9-1yEFGuEQIt5FtHuAM9VQjJXhhERY?usp=drive_link",
            
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
            "Trending apps",
            help="The top trending Streamlit apps",
            validate="^https://[a-z]+\.streamlit\.app$",
            max_chars=100,
        )
    },
    hide_index=True,
)
