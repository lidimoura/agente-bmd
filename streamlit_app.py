import streamlit as st
import json

# Configuração da página
st.set_page_config(page_title="Agente BMD", layout="wide", page_icon=":robot:")

# Cabeçalho
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("assets/logo_synk.png", width=80)
    with col2:
        st.title("Agente BMD")
        st.markdown("Apresentado pela **Synk AI** – Assistente inteligente para otimizar processos da Clínica BMD")

st.markdown("---")

# Dashboard de métricas
with st.container():
    st.header("Métricas Principais")
    with open("dashboard/dashboard_mock.json", "r") as f:
        dashboard = json.load(f)

    cols = st.columns(5)
    cols[0].metric("Tempo Economizado (mês)", dashboard["tempo_economizado_mes"])
    cols[1].metric("Custo Reduzido (mês)", dashboard["custo_reduzido_mes"])
    cols[2].metric("Pacientes atendidos a mais", dashboard["pacientes_atendidos_a_mais"])
    cols[3].metric("Eficiência projetada", dashboard["eficiencia_projetada"])
    cols[4].metric("Qualidade do tempo operacional", dashboard["qualidade_tempo_operacional"])

st.markdown("---")

# Webchat GPTMaker
st.header("Chat Interativo")
st.markdown("Converse com o agente BMD diretamente:")
st.markdown(
    '<iframe src="URL_DO_CHATGPTMAKER" width="100%" height="600px" style="border-radius:10px;"></iframe>',
    unsafe_allow_html=True
)

st.markdown("---")

# Rodapé
st.markdown(
    "Links Úteis: [Clínica BMD](https://clinicabmd.com.br) | [Synk AI](https://synk.ai) | [GitHub](https://github.com/lidimoura/agente-bmd)"
)
st.markdown(
    "Em breve, o projeto será configurado com Supabase para memória persistente e métricas avançadas."
)
