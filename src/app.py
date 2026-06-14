import json
import pandas as pd
import requests
import streamlit as st

# ======================================== CONFIGURAÇÃO ====================================
OLLAMA_URL = 'http://localhost:11434/v1/chat/completions'
# Preferred models in order (fallback sequence)
MODELOS = [
    'llama3:latest',
    'gemma4:latest',
    'gpt-oss:latest'
]

# ====================================== CARRREGAR DADOS ===================================
transacoes = pd.read_csv('data/transacoes.csv')
historico = pd.read_csv('data/historico_atendimento.csv')
perfil = json.load(open('data/perfil_investidor.json'))
produtos = json.load(open('data/produtos_financeiros.json'))

# ====================================== MONTAR CONTEXTO ===================================
contexto = f"""
USUARIO: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']},
OBJETIVO: {perfil['objetivo_principal']},

PATRIMONIO: R${perfil['patrimonio_total']}, RESERVA: R${perfil['reserva_emergencia_atual']}

TRASANAÇÕES RECENTES: {transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES: {historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS: {json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ====================================== SYSTEM PROMPT =======================================
SYSTEM_PROMPT = f"""Você é FinanBot, um agente financeiro inteligente especializado em educação financeira pessoal e planejamento de metas.

Seu objetivo é ajudar o usuário a:
- Organizar suas finanças pessoais
- Acompanhar gastos e receitas
- Planejar e atingir metas financeiras
- Entender produtos financeiros adequados ao seu perfil

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos (perfil, transações, gastos, histórico de atendimento, produtos financeiros).
2. Nunca invente informações financeiras ou valores que não estejam na base.
3. Se não souber algo, considerando apenas o conetúdo da pasta data, responda que não tem essa informação.
4. Use linguagem clara, acessível e educativa.
5. Sempre contextualize sugestões com o perfil do usuário (moderado, foco em reserva de emergência).
6. Não forneça informações sensíveis (senhas, dados pessoais de terceiros).
7. Incentive boas práticas financeiras: controle de gastos, diversificação, reserva de emergência.
8. Quando o usuário pedir recomendações, explique o raciocínio por trás da sugestão, mas não diga ao usuário para investir em ativos específicos.
9. Evite jargões técnicos sem explicação.
10. Respeite o limite de risco do usuário (não sugerir produtos incompatíveis com perfil).
11. Limite-se a responder especificamente o que foi perguntado, sem detalhes desnecessários, a menos que o usuário peça por mais informações.
"""
# 12. Forneça no final da sua resposta: Latência e tempo de resposta; Consumo de tokens e custos; Logs e taxa de erros.

# ====================================== CHAMAR OLLAMA =======================================

def gerar_resposta(mensagem_usuario):
    # limit context size to avoid very large payloads that may time out
    max_ctx = 3000
    contexto_enviado = contexto if len(contexto) <= max_ctx else contexto[:max_ctx] + "\n... (context truncated)"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"CONTEXT: {contexto_enviado}\n\nPERGUNTA: {mensagem_usuario}"},
    ]

    last_exception = None
    # prefer models that are actually available on the Ollama server
    try:
        avail = requests.get(OLLAMA_URL.replace('/v1/chat/completions', '/v1/models'), timeout=10)
        avail.raise_for_status()
        data = avail.json()
        available_ids = {m['id'] for m in data.get('data', []) if isinstance(m, dict) and 'id' in m}
        modelos_try = [m for m in MODELOS if m in available_ids]
        if not modelos_try:
            modelos_try = MODELOS
    except Exception:
        modelos_try = MODELOS

    for modelo in modelos_try:
        try:
            r = requests.post(
                OLLAMA_URL,
                json={
                    "model": modelo,
                    "messages": messages,
                    "temperature": 0.2,
                    "max_tokens": 400,
                },
                timeout=120,
            )
            r.raise_for_status()
            resposta = r.json()
            if isinstance(resposta, dict) and 'choices' in resposta and resposta['choices']:
                choice = resposta['choices'][0]
                if isinstance(choice, dict):
                    if 'message' in choice and isinstance(choice['message'], dict) and 'content' in choice['message']:
                        return choice['message']['content']
                    if 'text' in choice:
                        return choice['text']
            # If we reach here, return the raw response for inspection
            return f"⚠️ Resposta inesperada ({modelo}): {resposta}"
        except requests.exceptions.RequestException as e:
            last_exception = e
            # try next model
            continue

    if isinstance(last_exception, requests.exceptions.ConnectionError):
        return "❌ Não consegui conectar ao Ollama. Verifique se está rodando em localhost:11434"
    if last_exception:
        return f"❌ Erro ao chamar modelos: {str(last_exception)}"
    return "⚠️ Nenhuma resposta obtida dos modelos disponíveis."

# ==================================== INTERFACE STREAMLIT =====================================

if __name__ == "__main__":
    st.title("🤖 FinanBot - Seu Assistente Financeiro Pessoal")

    if pergunta := st.chat_input("Faça sua pergunta financeira..."):
        st.chat_message("user").write(pergunta)
        with st.spinner("Gerando resposta..."):
            st.chat_message("assistant").write(gerar_resposta(pergunta))