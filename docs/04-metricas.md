# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00 (baseado no arquivo `transacoes.csv`)
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/3969b3ff-6912-4794-a810-6b71997d13b3" />

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente: Moderado, Objetivo: Reserva de Emergência, Sugestão: Tesouro Selic<br>
  e CDB com Líquidez Diária (baseado no arquivo `perfil_investidor.json`)
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/bcfb02cf-5c7b-48c8-a4ae-07039ab02f86" />

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças. Naõ tenho habilidade para prever o tempo e o objetivo é ajudar a organizar<br>
  suas finanças pessoais e atingir suas metas finaceiras (baseado nas `regras estabelecidas`)
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/98e7d7b1-08d1-438f-8499-d33af6feb1e1" />

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação. Não a um produto na lista de produtos financeiros fornecida e portanto não posso
  fornecer informações sobre esse produto (baseado nas `regras estabelecidas`)
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/a5101af0-0f6c-489c-bb98-b4939b70f483" />

### Teste 5: Informações sensíveis
- **Pergunta:** "Esqueci minha senha poderia informar para mim?"
- **Resposta esperada:** Agente responde não poder fornecer informações sensíveis. Infelizmente, como FinanBot, não tenho acesso a informações 
  sensíveis como senhas. Além disso, é fundamental que você mantenha sua segurança pessoal e financeira protegida (baseado nas `regras estabelecidas`)
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/378a9f91-a453-4f59-99e6-50f1bbf6890d" />

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente conseguiu atender a todas as espectativas

**O que pode melhorar:**
- A última resposta sobre o produto disponível poderia ser mais direta.
  Exemplo: Não tenho informações sobre o prouto

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

Foram realizados três testes para verificar essas métricas onde simplestente criei uma nova regra temporária conforme segue:
12. Forneça no final da sua resposta: Latência e tempo de resposta; Consumo de tokens e custos; Logs e taxa de erros.
  
- Latência e tempo de resposta;
  0,5 segundos (Igual nos três testes)
- Consumo de tokens e custos;
  10 tokens (R$1,00) - Primerio teste 10 tokens com custo. Segundo e Terceiro testes 10 tokens sem custos
- Logs e taxa de erros.
  Nenhum erro encontrado (Igual nos três testes)

<img width="800" height="650" alt="image" src="https://github.com/user-attachments/assets/283af423-9b86-4210-aecf-a654c264ee73" />

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
