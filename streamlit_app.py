import streamlit as st

st.set_page_config(page_title="Agente BMD", layout="wide", page_icon="🤖")

# Cabeçalho
st.image("assets/logo_bmd.png", width=80)
st.title("Agente BMD")
st.markdown("Apresentado pela **Synk AI** – Assistente inteligente para otimizar processos na Clínica BMD")

st.markdown("---")

# Sobre o Agente
st.subheader("Sobre o Agente BMD")
st.markdown("""
O **Agente BMD** ajuda a equipe da clínica a:
- Obter informações rápidas e precisas
- Melhorar eficiência operacional
- Evoluir continuamente com base nas interações
""")

# Evolução
st.subheader("Evolução do Projeto")
st.markdown("""
- **Protótipo Typebot**: Primeira versão de teste  
- **GPTMaker Bubble**: Chat interativo atual  
- **Próximos passos**: Melhorias contínuas e memória persistente
""")

st.markdown("---")

# Call-to-Action
st.subheader("Converse com o Agente BMD")
st.markdown(
    "[Clique aqui para abrir o chat](https://app.gptmaker.ai/widget/3E6A303F3BAA7072AAC7C247DD2D37A8/float.js)"
)
st.markdown("O chat abrirá em float no canto inferior direito, pronto para interagir com você!")

st.markdown("---")

# Rodapé
st.markdown(
    "Links úteis: [Clínica BMD](https://clinicabmd.com.br) | [Synk AI](https://synk.ai) | [GitHub](https://github.com/lidimoura/agente-bmd)"
)
