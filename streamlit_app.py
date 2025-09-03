import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(
    page_title="Agente BMD",
    layout="wide",
    page_icon="🤖"
)

# Título opcional acima do chat
st.title("Agente BMD – Chat Interativo")
st.markdown("Converse diretamente com o agente BMD usando o chat abaixo:")

# Embed do GPTMaker float chat
components.html("""
<script async src="https://app.gptmaker.ai/widget/3E6A303F3BAA7072AAC7C247DD2D37A8/float.js"></script>
""", height=700)  # ajuste a altura se necessário
