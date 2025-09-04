# Projeto Synk – BMD (Assistente de Clínica de Imagem)  

## *Briefing do Projeto*
- **Nome do projeto:** Synk – BMD (Assistente Inteligente)  
- **Objetivo principal:** Criar um agente virtual humanizado no WhatsApp que informa horários de funcionamento, orienta sobre exames e apoia no pré-atendimento, com linguagem regional e acessível.  
- **Stakeholders envolvidos:** Diretoria/coordenação da BMD, equipe de recepção, Synk (time interno).  
- **Stack/Ferramentas:** Typebot, Make/n8n, OpenAI API, Supabase (dados e dashboards), Streamlit (painéis).  

*Ponto de partida:*  
- Diagnóstico inicial feito  
- Dois formulários Typebot criados (funcionários + coordenação/diretoria)  
- Primeiros protótipos de linguagem e fluxo estruturados  

---

## *Metas e Indicadores*
**Metas SMART**  
- Entregar primeiro protótipo do agente até setembro/25.  
- Mapear 100% do fluxo de perguntas frequentes dos funcionários até o final do onboarding.  
- Criar dashboard com métricas básicas (interações, perguntas respondidas, principais dúvidas) até fase 3.  

**Indicadores de sucesso**  
- Redução de tempo da recepção em responder dúvidas simples.  
- Satisfação da equipe com o agente superior a 80% (feedback).  
- Clareza e consistência nas informações dadas pelo bot.  

---

## *Estrutura e Recursos*
**Fluxos planejados**  
- Recepção inicial (boas-vindas + filtro da necessidade).  
- FAQ sobre horários, documentos e preparo de exames.  
- Encaminhamento para humano quando necessário.  

**Recursos existentes**  
- Formulários de diagnóstico (Typebot).  
- Reunião inicial registrada em anotações.  

**A construir**  
- Base de dados Supabase.  
- Dashboard de monitoramento.  
- Script inicial no Typebot.  

---

## *Roadmap / Linha do Tempo*
- Julho/25 → Diagnóstico inicial  
- Julho/25 → Estruturação dos formulários Typebot  
- Agosto/25 → Discussão sobre integração Supabase + dashboards  
- Setembro/25 → Preparação para protótipo 1  
- Integração Supabase (dados de interações)  
- Testes internos com equipe da clínica  
- Criação de dashboards (Streamlit ou Supabase)  
- Ajustes de linguagem e funcionalidades  
- Entrega oficial para diretoria  
- Ciclo de evolução contínua  

---

## *Histórico de Evolução*
- Julho/25 – Diagnóstico inicial da clínica  
- Julho/25 – Estruturação dos dois formulários no Typebot  
- Agosto/25 – Discussão sobre integração Supabase e dashboards  
- Setembro/25 – Preparação para protótipo 1  

---

## *Próximos Passos*
- [ ] Finalizar protótipo 1 no Typebot com base nos formulários  
- [ ] Configurar banco **Supabase** para armazenamento de interações  
- [ ] Estruturar primeiros indicadores no dashboard  
- [ ] Criar três variações de mensagem de boas-vindas (testar tom de voz)  
- [ ] Definir perguntas frequentes com base nos formulários  
- [ ] Configurar webhook Typebot → Supabase  

---

## *Insights e Aprendizados*
- Linguagem **regional e humanizada** gera maior conexão com pacientes  
- A equipe valoriza **clareza e simplicidade** acima de excesso de funções  
- Importante pensar em um **handoff eficiente** (bot → humano)  

---

## *Visão de Futuro*
- Modelo replicável para outras clínicas de saúde  
- Case de **Customer Success** para a Synk, mostrando impacto real  
- Base para um **SaaS white-label** (assistente humanizado para clínicas regionais)  
