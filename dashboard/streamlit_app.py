import streamlit as st
import json

st.set_page_config(page_title="Agente BMD", layout="wide")
st.title("Painel do Agente BMD")

# Carregar métricas do dashboard
with open("dashboard/dashboard_mock.json", "r") as f:
    dashboard = json.load(f)

# Seção de métricas principais
st.header("Métricas Principais")
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Tempo Economizado (mês)", dashboard["tempo_economizado_mes"])
col2.metric("Custo Reduzido (mês)", dashboard["custo_reduzido_mes"])
col3.metric("Pacientes atendidos a mais", dashboard["pacientes_atendidos_a_mais"])
col4.metric("Eficiência projetada", dashboard["eficiencia_projetada"])
col5.metric("Qualidade do tempo operacional", dashboard["qualidade_tempo_operacional"])

# Protótipos disponíveis
st.header("Protótipos Disponíveis")
st.markdown("[Abrir Typebot](https://typebot.co/open-ai-assistant-chat-ipijrev)")
st.markdown("[Abrir GPTMaker](#)")  # Substituir pelo link real do GPTMaker

# Observações e futuro
st.header("Observações")
st.markdown(
    "Em breve, o projeto será configurado com Supabase, garantindo memória persistente, histórico de interações e métricas. "
    "O foco é implementar automações e melhorias nos processos da clínica para garantir maior eficiência e melhor qualidade de tempo operacional."
)
