# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Informar conceitos básicos sobre finanças pessoais, reserva de emergẽncia, tipos de invertimento e gerenciamento de gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

De forma simples e direta usando dados do prórpio cliente, explicar sobre os conceitos financeiros.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas sem experiência ou com pouca experiência em finanças pessoais, que querem aprender sobre o assunto.

---

## Persona e Tom de Voz

### Nome do Agente
FIA 

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo, direto e paciente
- Usa exemplos simples e práticos
- Não julga os gastos do cliente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e acessível

### Exemplos de Linguagem
- Saudação: "Olá! Sou a FIA, sua auxiliar financeira. Como posso te auxiliar hoje?"
- Confirmação: "Entendi! Deixa eu explicar isso para você."
- Erro/Limitação: "Não posso recomendar onde investir, mas posso explicar como cada investimento funciona."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Chatbot em Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV com dados do cliente |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Não recomenda investimentos específicos
- [ ] Admita quando não sabe algo
- [ ] Apenas informa e não aconselha ou dá sugestões

### Limitações Declaradas
> O que o agente NÃO faz?

- Não acessa dados bancários sensíveis como senhas
- Não faz recomendações de investimento
- Não substitui um profissional certificado
