# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no FinanBot |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, dar continuidade no atendimento de forma mais eficiente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas apresentadas |
| `produtos_financeiros.json` | JSON | Conhecer os proutos disponívels para que possam ser ensinados ao usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do usuário e usar essas informações|
| `gastos_mensais.csv` | CSV | Analisar padrão de gastos pessoais mensais e usar essas informações|

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto Fundo multimercado foi substituido por Fundo imobiliário, que é menos arriscado que fundos multimercados

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt.
Existem duas possibilidades, inserir os dados direto no prompt (Ctrl + c e Ctrl + v) ou carregar os arquivos via código, como no exemplo abaixo (recomendado)

```python
# Importação das bibliotecas necessárias
import pandas as pd   # Biblioteca para manipulação de dados em tabelas (DataFrames)
import json           # Biblioteca para trabalhar com arquivos JSON

# -----------------------------
# Leitura de arquivos CSV
# -----------------------------

# Lendo o arquivo de gastos mensais
gastos_mensais = pd.read_csv("gastos_mensais.csv")

# Lendo o arquivo de histórico de atendimento
historico_atendimento = pd.read_csv("historico_atendimento.csv")

# Lendo o arquivo de transações
transacoes = pd.read_csv("transacoes.csv")

# -----------------------------
# Leitura de arquivos JSON
# -----------------------------

# Lendo o arquivo de produtos financeiros
with open("produtos_financeiros.json", encoding="utf-8") as f:
    produtos_financeiros = json.load(f)

# Lendo o arquivo de perfil do investidor
with open("perfil_investidor.json", encoding="utf-8") as f:
    perfil_investidor = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
Dados do usuário:


Perfil do usuário:

Transações do usuário:

Histórico de atendimento do usuário:

Gastos do usuário:

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
