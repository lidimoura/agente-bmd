import streamlit as st
import pandas as pd
import datetime
import time
import random
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração inicial
st.set_page_config(
    page_title="BMD Assistente - Synk", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏥"
)

# CSS customizado para melhorar visual
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .status-active { color: #28a745; font-weight: bold; }
    .status-pending { color: #ffc107; font-weight: bold; }
    .status-resolved { color: #6c757d; font-weight: bold; }
    .status-cancelled { color: #dc3545; font-weight: bold; }
    .chat-message {
        background: #f8f9fa;
        padding: 0.5rem;
        border-left: 4px solid #007bff;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
    .header-synk {
        background: linear-gradient(90deg, #2196F3, #21CBF3);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="header-synk">
    <h1>🏥 BMD Assistente - Dashboard Synk</h1>
    <p>Protótipo • Assistente de Agendamento Inteligente via GPTMaker + Web Chat</p>
    <small>Desenvolvido em Manaus 🌿</small>
</div>
""", unsafe_allow_html=True)

# Função para gerar dados simulados em tempo real
@st.cache_data(ttl=5)  # Cache por 5 segundos para simular tempo real
def gerar_dados_tempo_real():
    pacientes = ["Maria Silva", "José Santos", "Ana Costa", "Carlos Oliveira", "Fernanda Lima", "João Pereira"]
    mensagens = [
        "Preciso remarcar meu exame", "Qual o valor do ultrassom?", "Obrigada pelo atendimento!",
        "Posso trazer acompanhante?", "Preciso fazer jejum?", "Como funciona a ressonância?",
        "Aceita convênio?", "Horário disponível amanhã?", "Resultado já saiu?"
    ]
    status_chat = ["Em andamento", "Aguardando resposta", "Resolvido", "Finalizado"]
    
    conversas = pd.DataFrame({
        "Paciente": random.choices(pacientes, k=5),
        "Última mensagem": random.choices(mensagens, k=5),
        "Status": random.choices(status_chat, k=5),
        "Horário": [(datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 60))).strftime("%H:%M:%S") for _ in range(5)],
        "Canal": random.choices(["Web Chat", "WhatsApp", "Telefone"], k=5)
    })
    
    exames = ["Ressonância Magnética", "Raio-X", "Ultrassom", "Tomografia", "Mamografia", "Densitometria"]
    status_agendamento = ["Confirmado", "Pendente", "Cancelado", "Em andamento"]
    
    agendamentos = pd.DataFrame({
        "Paciente": random.choices(pacientes, k=8),
        "Data": [(datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))).strftime("%d/%m/%Y") for _ in range(8)],
        "Horário": [f"{random.randint(8, 17):02d}:{random.choice(['00', '30'])}" for _ in range(8)],
        "Exame": random.choices(exames, k=8),
        "Status": random.choices(status_agendamento, k=8),
        "Valor": [f"R$ {random.randint(150, 800)},00" for _ in range(8)]
    })
    
    return conversas, agendamentos

# Função para métricas em tempo real
def calcular_metricas(conversas, agendamentos):
    conversas_ativas = len(conversas[conversas['Status'].isin(['Em andamento', 'Aguardando resposta'])])
    agendamentos_pendentes = len(agendamentos[agendamentos['Status'] == 'Pendente'])
    taxa_resolucao = round(len(conversas[conversas['Status'] == 'Resolvido']) / len(conversas) * 100, 1) if len(conversas) > 0 else 0
    total_agendamentos_hoje = len(agendamentos[agendamentos['Data'] == datetime.date.today().strftime("%d/%m/%Y")])
    
    return conversas_ativas, agendamentos_pendentes, taxa_resolucao, total_agendamentos_hoje

# Sidebar para navegação
st.sidebar.image("https://via.placeholder.com/200x80/2196F3/white?text=SYNK+AI", width=200)
st.sidebar.markdown("---")
aba = st.sidebar.radio(
    "🧭 Navegação", 
    ["📊 Visão Geral", "💬 Chats em Tempo Real", "📅 Agendamentos", "📈 Analytics", "⚙️ Configurações"],
    index=0
)

# Auto-refresh
if st.sidebar.button("🔄 Atualizar Dados"):
    st.rerun()

# Checkbox para auto-refresh
auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh (5s)", value=False)
if auto_refresh:
    time.sleep(5)
    st.rerun()

# Gerar dados
conversas, agendamentos = gerar_dados_tempo_real()
conversas_ativas, agendamentos_pendentes, taxa_resolucao, agendamentos_hoje = calcular_metricas(conversas, agendamentos)

# Conteúdo das abas
if aba == "📊 Visão Geral":
    st.subheader("📋 Resumo Executivo - BMD Assistente")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💬 Conversas Ativas", 
            value=conversas_ativas,
            delta=f"+{random.randint(1, 3)} hoje"
        )
    
    with col2:
        st.metric(
            label="📅 Agendamentos Pendentes", 
            value=agendamentos_pendentes,
            delta=f"-{random.randint(0, 2)} resolvidos"
        )
    
    with col3:
        st.metric(
            label="✅ Taxa de Resolução", 
            value=f"{taxa_resolucao}%",
            delta=f"+{random.randint(1, 5)}% vs. ontem"
        )
    
    with col4:
        st.metric(
            label="🏥 Exames Hoje", 
            value=agendamentos_hoje,
            delta="Dentro do planejado"
        )
    
    st.markdown("---")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Status das Conversas")
        status_counts = conversas['Status'].value_counts()
        fig_pie = px.pie(
            values=status_counts.values, 
            names=status_counts.index,
            color_discrete_sequence=['#28a745', '#ffc107', '#6c757d', '#007bff']
        )
        fig_pie.update_layout(showlegend=True, height=300)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("📈 Exames por Tipo")
        exame_counts = agendamentos['Exame'].value_counts()
        fig_bar = px.bar(
            x=exame_counts.index, 
            y=exame_counts.values,
            color=exame_counts.values,
            color_continuous_scale='Blues'
        )
        fig_bar.update_layout(showlegend=False, height=300, xaxis_tickangle=45)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Últimas atividades
    st.subheader("🔔 Atividades Recentes")
    atividades_recentes = conversas.head(3)
    for _, conversa in atividades_recentes.iterrows():
        status_class = {
            'Em andamento': 'status-active',
            'Aguardando resposta': 'status-pending', 
            'Resolvido': 'status-resolved',
            'Finalizado': 'status-resolved'
        }.get(conversa['Status'], 'status-pending')
        
        st.markdown(f"""
        <div class="chat-message">
            <strong>{conversa['Paciente']}</strong> • <span class="{status_class}">{conversa['Status']}</span><br>
            <em>"{conversa['Última mensagem']}"</em><br>
            <small>📱 {conversa['Canal']} • ⏰ {conversa['Horário']}</small>
        </div>
        """, unsafe_allow_html=True)

elif aba == "💬 Chats em Tempo Real":
    st.subheader("💬 Conversas em Andamento")
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.selectbox("Filtrar por Status", ["Todos"] + list(conversas['Status'].unique()))
    with col2:
        canal_filter = st.selectbox("Filtrar por Canal", ["Todos"] + list(conversas['Canal'].unique()))
    with col3:
        st.metric("Total de Conversas", len(conversas))
    
    # Aplicar filtros
    df_filtrado = conversas.copy()
    if status_filter != "Todos":
        df_filtrado = df_filtrado[df_filtrado['Status'] == status_filter]
    if canal_filter != "Todos":
        df_filtrado = df_filtrado[df_filtrado['Canal'] == canal_filter]
    
    # Tabela interativa
    st.dataframe(
        df_filtrado,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Status": st.column_config.SelectboxColumn(
                "Status",
                options=["Em andamento", "Aguardando resposta", "Resolvido", "Finalizado"]
            ),
            "Canal": st.column_config.SelectboxColumn(
                "Canal", 
                options=["Web Chat", "WhatsApp", "Telefone"]
            )
        }
    )
    
    # Simulador de nova mensagem
    if st.button("📥 Simular Nova Mensagem"):
        st.success("Nova mensagem recebida de Maria Silva: 'Gostaria de confirmar meu exame para amanhã'")
        time.sleep(1)
        st.rerun()

elif aba == "📅 Agendamentos":
    st.subheader("📅 Gestão de Agendamentos")
    
    # Estatísticas rápidas
    col1, col2, col3 = st.columns(3)
    with col1:
        confirmados = len(agendamentos[agendamentos['Status'] == 'Confirmado'])
        st.metric("✅ Confirmados", confirmados)
    with col2:
        pendentes = len(agendamentos[agendamentos['Status'] == 'Pendente'])
        st.metric("⏳ Pendentes", pendentes)
    with col3:
        cancelados = len(agendamentos[agendamentos['Status'] == 'Cancelado'])
        st.metric("❌ Cancelados", cancelados)
    
    # Filtro por data
    col1, col2 = st.columns(2)
    with col1:
        data_inicial = st.date_input("Data Inicial", datetime.date.today())
    with col2:
        data_final = st.date_input("Data Final", datetime.date.today() + datetime.timedelta(days=30))
    
    # Tabela de agendamentos
    st.dataframe(
        agendamentos,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Status": st.column_config.SelectboxColumn(
                "Status",
                options=["Confirmado", "Pendente", "Cancelado", "Em andamento"]
            ),
            "Valor": st.column_config.TextColumn("Valor")
        }
    )

elif aba == "📈 Analytics":
    st.subheader("📈 Analytics e Insights")
    
    # Gráfico de timeline
    st.subheader("📊 Conversas por Horário")
    # Simular dados por hora
    horas = list(range(8, 18))
    conversas_por_hora = [random.randint(5, 25) for _ in horas]
    
    fig_timeline = go.Figure()
    fig_timeline.add_trace(go.Scatter(
        x=[f"{h}:00" for h in horas],
        y=conversas_por_hora,
        mode='lines+markers',
        name='Conversas',
        line=dict(color='#2196F3', width=3),
        marker=dict(size=8)
    ))
    fig_timeline.update_layout(
        title="Distribuição de Conversas por Horário",
        xaxis_title="Horário",
        yaxis_title="Número de Conversas",
        height=400
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Insights automáticos
    st.subheader("🧠 Insights Automáticos")
    insights = [
        "🔥 Pico de conversas entre 14h-16h (horário de almoço)",
        "📱 85% das conversas vêm do Web Chat",
        "⚡ Tempo médio de resposta: 2.5 minutos",
        "📅 Ultrassom é o exame mais agendado (35%)",
        "✅ Taxa de confirmação de agendamentos: 92%"
    ]
    
    for insight in insights:
        st.info(insight)

elif aba == "⚙️ Configurações":
    st.subheader("⚙️ Configurações do Sistema")
    
    # Status do sistema
    st.subheader("🔧 Status do Sistema")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("✅ GPTMaker - Online")
        st.info("🔗 API Status: Conectada")
    
    with col2:
        st.success("✅ Web Chat - Ativo")
        st.warning("⚠️ WhatsApp - Em desenvolvimento")
    
    with col3:
        st.success("✅ Supabase - Conectado")
        st.info("📊 Dashboard - Online")
    
    st.markdown("---")
    
    # Configurações
    st.subheader("🌐 Configurações de Deploy")
    
    col1, col2 = st.columns(2)
    with col1:
        dominio = st.text_input(
            "Domínio Synk (quando disponível):", 
            value="bmd-assistente.synk.ai",
            help="Domínio onde o agente ficará hospedado"
        )
        
        ambiente = st.selectbox(
            "Ambiente:",
            ["Desenvolvimento (Streamlit)", "Produção (Synk Domain)"]
        )
    
    with col2:
        webhook_url = st.text_input(
            "Webhook URL (GPTMaker):",
            value="https://api.gptmaker.ai/webhook/bmd-assistant"
        )
        
        supabase_url = st.text_input(
            "Supabase Project URL:",
            value="https://seu-projeto.supabase.co"
        )
    
    if dominio:
        st.success(f"🌐 Agente estará disponível em: `https://{dominio}`")
    
    # Configurações avançadas
    with st.expander("🔧 Configurações Avançadas"):
        st.checkbox("📧 Notificações por email", value=True)
        st.checkbox("📱 Notificações push", value=False) 
        st.selectbox("🕒 Fuso horário", ["America/Manaus", "America/Sao_Paulo"], index=0)
        st.slider("⏱️ Timeout de sessão (minutos)", 5, 60, 30)
        st.number_input("📊 Limite de conversas simultâneas", 1, 100, 50)
    
    # Botões de ação
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Deploy para Produção", type="primary"):
            st.success("Deploy iniciado! Aguarde...")
            
    with col2:
        if st.button("💾 Salvar Configurações"):
            st.success("Configurações salvas com sucesso!")
            
    with col3:
        if st.button("🔄 Reiniciar Sistema"):
            st.info("Sistema será reiniciado em 10 segundos...")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>BMD Assistente Dashboard</strong> | Desenvolvido por Synk em Manaus 🌿</p>
    <p>Versão 1.0 • Protótipo | Powered by Streamlit + GPTMaker + Supabase</p>
</div>
""", unsafe_allow_html=True)
