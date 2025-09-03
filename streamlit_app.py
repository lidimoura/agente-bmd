import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Agente BMD", layout="wide", page_icon="🤖")

st.title("Agente BMD")

# Controle para carregar o chat apenas uma vez
if "chat_loaded" not in st.session_state:
    st.session_state.chat_loaded = False

if st.button("Iniciar Chat") or st.session_state.chat_loaded:
    st.session_state.chat_loaded = True
    gptmaker_url = "URL_DO_SEU_CHATGPTMAKER"
    components.html(
        f'<iframe src="{gptmaker_url}" width="100%" height="700px" style="border-radius:10px; border:none;"></iframe>',
        height=700
    )
