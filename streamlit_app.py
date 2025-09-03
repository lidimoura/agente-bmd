import streamlit as st
import streamlit.components.v1 as components

# ------------------------------
# Configuração da página
# ------------------------------
st.set_page_config(
    page_title="Agente BMD",
    layout="wide",
    page_icon="🤖"
)

# ------------------------------
# Cabeçalho / Hero
# ------------------------------
with st.container():
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("assets/logo_bmd.png", width=80)
    with col2:
        st.title("Agente BMD")
        st.markdown(
            "Apresentado pela **Synk AI** – Seu assistente inteligente para otimizar processos na Clínica BMD."
        )

st.markdown("---")

# ------------------------------
# Sobre o Agente
# ------------------------------
with st.expander("Sobre o Agente BMD", expanded=True):
    st.markdown("""
    O **Agente BMD** foi desenvolvido para:
    - Auxiliar a equipe da clínica com informações rápidas e precisas.
    - Garantir **maior eficiência operacional** e melhor qualidade de tempo.
    - Evoluir continuamente com base nas interações e feedback.
    """)

# ------------------------------
# Evolução do projeto
# ------------------------------
with st.expander("Evolução do Agente", expanded=False):
    st.markdown("""
    **Linha do tempo do projeto:**
    1. **Protótipo Typebot** – Coleta inicial de informações.
    2. **GPTMaker Bubble** – Chat interativo com respostas humanizadas.
    3. **Próximos Passos** – Integração com memória persistente, automações e melhorias contínuas.
    """)

st.markdown("---")

# ------------------------------
# Call to Action para iniciar o chat
# ------------------------------
st.header("Converse com o Agente BMD")
st.markdown("Clique no botão abaixo para abrir o chat interativo:")

if st.button("Iniciar Chat"):
    # Substitua pela URL do seu webchat GPTMaker
    gptmaker_url = "URL_DO_SEU_CHATGPTMAKER"
    components.html(
        f"""
        <iframe src="{gptmaker_url}" width="100%" height="700px" style="border-radius:10px; border:none;"></iframe>
        """,
        height=700
    )

st.markdown("---")

# ------------------------------
# Rodapé
# ------------------------------
st.markdown(
    "Links Úteis: [Clínica BMD](https://clinicabmd.com.br) | [Synk AI](https://synk.ai) | [GitHub](https://github.com/lidimoura/agente-bmd)"
)
st.markdown(
    "Em breve, o projeto será configurado com Supabase para memória persistente e métricas avançadas."
)
