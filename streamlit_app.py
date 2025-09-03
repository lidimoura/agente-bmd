import streamlit as st

st.set_page_config(page_title="Agente BMD", layout="wide", page_icon="🤖")

st.image("assets/logo_bmd.png", width=80)
st.title("Agente BMD")
st.markdown("Apresentado pela **Synk AI** – Assistente inteligente para otimizar processos na Clínica BMD")

st.markdown("---")

st.subheader("Converse com o Agente BMD")
st.markdown(
    '[Clique aqui para abrir o chat](https://app.gptmaker.ai/widget/3E6A303F3BAA7072AAC7C247DD2D37A8/float.js)',
    unsafe_allow_html=True
)
st.markdown("O chat vai abrir em float no canto inferior direito.")
