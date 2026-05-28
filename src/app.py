import json
import pandas as pd

# Carregar dados
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# Montar contexto
contexto = f'''
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, pefil {perfil['pefil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES: {historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, index=2, ensure_ascii=False)}
'''

# System prompt

SYSTEM_PROMPT = ''' Você é a FIA, uma educadora financeira amigável e didática.

OBJETIVO: 
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como 
exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funciona.
- NUNCA responda a perguntas fora do tema de finanças pessoais.
- Quando ocorrer, responda lembrando o seu papel de educadora financeira.
- Use os dados fornecidos para dar exemplos personalizados.
- Use linguagem simples e direta ao ponto.
- Se não souber algo, admita: "Não possuo essa informação..."
- Sempre pegunte se o cliente entendeu.
- Dê respostas com no máximo 3 parágrafos.
'''
