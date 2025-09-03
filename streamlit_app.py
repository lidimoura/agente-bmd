import streamlit as st
import json

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
    col1, col2 = st.columns([1,4])
    with col1:
        st.image("assets/logo_bmd.png", width=80)
    with col2:
        st.title("Agente BMD")
        st.markdown(
            "Apresentado pela **Synk AI** – Assistente inteligente para otimizar processos da Clínica BMD"
        )

st.markdown("---")

# ------------------------------
# Evolução do projeto
# ------------------------------
st.header("Evolução do Agente BMD")
st.markdown("""
| Etapa | Descrição |
|-------|-----------|
| Protótipo Typebot | Primeira versão do agente, focada em coleta de informações básicas |
| GPTMaker Bubble | Versão atual, chat interativo com estilo bubble e respostas humanizadas |
| Próximos Passos | Melhorias na automação, memória persistente e integração com Supabase |
""")

st.markdown("---")

# ------------------------------
# Métricas principais
# ------------------------------
st.header("Métricas Simuladas")
with open("dashboard/dashboard_mock.json", "r") as f:
    dashboard = json.load(f)

cols = st.columns(5)
cols[0].metric("Tempo Economizado (mês)", dashboard.get("tempo_economizado_mes", "N/A"))
cols[1].metric("Custo Reduzido (mês)", dashboard.get("custo_reduzido_mes", "N/A"))
cols[2].metric("Pacientes atendidos a mais", dashboard.get("pacientes_atendidos_a_mais", "N/A"))
cols[3].metric("Eficiência projetada", dashboard.get("eficiencia_projetada", "N/A"))
cols[4].metric("Qualidade do tempo operacional", dashboard.get("qualidade_tempo_operacional", "N/A"))

st.markdown("---")

# ------------------------------
# Chat Interativo GPTMaker
# ------------------------------
st.header("Converse com o Agente BMD")
st.markdown("Use o chat abaixo para interagir com o agente em estilo bubble:")

# Substitua pela URL do seu webchat bubble GPTMaker
gptmaker_url = "<script 
 async 
 src="https://app.gptmaker.ai/widget/3E6A303F3BAA7072AAC7C247DD2D37A8/float.js">
</script>"

st.markdown(
    f'<iframe src="{gptmaker_url}" width="100%" height="600px" style="border-radius:10px;"></iframe>',
    unsafe_allow_html=True
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
