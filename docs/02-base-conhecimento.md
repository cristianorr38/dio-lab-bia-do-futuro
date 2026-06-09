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

O produto Fundo multimercado foi substituido por Fundo imobiliário, que é menos arriscado que fundos multimercados.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt.
Existem duas possibilidades, inserir os dados direto no prompt (Ctrl + c e Ctrl + v) ou carregar os arquivos via código, como no exemplo abaixo (recomendado).

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

Como forma de simplificar podemos **inserir** os dados em nosso prompt, garantidno o melhor contexto possível.
Em soluções maiores o ideal é que as informações sejam carregadas dinâmicamente tornando o processo mais rápido e flexível.

```text
Dados edo usuário e Perfil (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

Transações do usuário (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

Histórico de atendimento do usuário (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

Gastos do usuário (data/gastos_mensais.csv):
Categoria,Nome,Valor
Contas,Luz - Janeiro,230.00
Contas,Água - Janeiro,110.00
Contas,Internet - Janeiro,95.00
Contas,Celular - Janeiro,75.00
Contas,Luz - Fevereiro,240.00
Contas,Água - Fevereiro,115.00
Contas,Internet - Fevereiro,100.00
Contas,Celular - Fevereiro,80.00
Contas,Luz - Março,250.00
Contas,Água - Março,120.00
Contas,Internet - Março,105.00
Contas,Celular - Março,85.00
Contas,Luz - Abril,245.00
Contas,Água - Abril,118.00
Contas,Internet - Abril,102.00
Contas,Celular - Abril,82.00
Contas,Luz - Maio,255.00
Contas,Água - Maio,122.00
Contas,Internet - Maio,106.00
Contas,Celular - Maio,86.00
Contas,Luz - Junho,260.00
Contas,Água - Junho,125.00
Contas,Internet - Junho,108.00
Contas,Celular - Junho,88.00
Contas,Luz - Julho,265.00
Contas,Água - Julho,128.00
Contas,Internet - Julho,110.00
Contas,Celular - Julho,90.00
Contas,Luz - Agosto,270.00
Contas,Água - Agosto,130.00
Contas,Internet - Agosto,112.00
Contas,Celular - Agosto,92.00
Contas,Luz - Setembro,275.00
Contas,Água - Setembro,132.00
Contas,Internet - Setembro,114.00
Contas,Celular - Setembro,94.00
Contas,Luz - Outubro,280.00
Contas,Água - Outubro,135.00
Contas,Internet - Outubro,116.00
Contas,Celular - Outubro,96.00
Contas,Luz - Novembro,285.00
Contas,Água - Novembro,138.00
Contas,Internet - Novembro,118.00
Contas,Celular - Novembro,98.00
Contas,Luz - Dezembro,290.00
Contas,Água - Dezembro,140.00
Contas,Internet - Dezembro,120.00
Contas,Celular - Dezembro,100.00
Combustível,Gasolina - Janeiro,500.00
Combustível,Gasolina - Fevereiro,520.00
Combustível,Gasolina - Março,540.00
Combustível,Gasolina - Abril,560.00
Combustível,Gasolina - Maio,580.00
Combustível,Gasolina - Junho,600.00
Combustível,Gasolina - Julho,620.00
Combustível,Gasolina - Agosto,640.00
Combustível,Gasolina - Setembro,660.00
Combustível,Gasolina - Outubro,680.00
Combustível,Gasolina - Novembro,700.00
Combustível,Gasolina - Dezembro,720.00
Mercado,Supermercado - Janeiro,1400.00
Mercado,Supermercado - Fevereiro,1450.00
Mercado,Supermercado - Março,1500.00
Mercado,Supermercado - Abril,1520.00
Mercado,Supermercado - Maio,1550.00
Mercado,Supermercado - Junho,1580.00
Mercado,Supermercado - Julho,1600.00
Mercado,Supermercado - Agosto,1620.00
Mercado,Supermercado - Setembro,1650.00
Mercado,Supermercado - Outubro,1680.00
Mercado,Supermercado - Novembro,1700.00
Mercado,Supermercado - Dezembro,1750.00
Passeios,Viagem - Janeiro,1800.00
Passeios,Shopping - Janeiro,250.00
Passeios,Praia - Janeiro,120.00
Passeios,Shopping - Fevereiro,280.00
Passeios,Viagem - Março,2200.00
Passeios,Praia - Março,180.00
Passeios,Shopping - Abril,290.00
Passeios,Praia - Maio,190.00
Passeios,Shopping - Junho,320.00
Passeios,Viagem - Julho,2500.00
Passeios,Praia - Julho,210.00
Passeios,Shopping - Agosto,340.00
Passeios,Praia - Agosto,220.00
Passeios,Shopping - Setembro,350.00
Passeios,Shopping - Outubro,350.00
Passeios,Viagem - Novembro,2500.00
Passeios,Praia - Novembro,150.00
Passeios,Viagem - Dezembro,2000.00
Passeios,Shopping - Dezembro,550.00
Passeios,Praia - Dezembro,300.00

Produtos financeiros (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "6% a 12% a.a.",
    "aporte_minimo": "entre 10.00 a 100.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Usuárioe e Perfil
- Nome: João Silva, 32 anos
- Profissão: Analista de Sistemas
- Renda mensal: R$ 5.000,00
- Patrimônio total: R$ 15.000,00
- Reserva de emergência atual: R$ 10.000,00
- Perfil investidor: Moderado (não aceita risco)
- Objetivo principal: Construir reserva de emergência
- Metas financeiras:
- Completar reserva de emergência (R$ 15.000, prazo: jun/2026)
- Entrada de apartamento (R$ 50.000, prazo: dez/2027)

Transações Recentes (Outubro/2025)

    Receita: Salário R$ 5.000,00

    Principais despesas:

        Moradia: Aluguel R$ 1.200, Luz R$ 180

        Alimentação: Supermercado R$ 450, Restaurante R$ 120

        Lazer: Netflix R$ 55,90

        Saúde: Farmácia R$ 89, Academia R$ 99

        Transporte: Uber R$ 45, Combustível R$ 250

📞 Histórico de Atendimento

    Perguntas sobre CDB e Tesouro Selic

    Problema técnico no app resolvido

    Acompanhamento de metas financeiras (reserva de emergência)

    Atualização cadastral (e-mail e telefone)

📊 Gastos Mensais (2025)

    Contas fixas: Luz (R$ 230 → R$ 290 ao longo do ano), Água (R$ 110 → R$ 140), Internet (R$ 95 → R$ 120), Celular (R$ 75 → R$ 100)

    Combustível: Crescente de R$ 500 (jan) até R$ 720 (dez)

    Supermercado: R$ 1.400 (jan) até R$ 1.750 (dez)

    Passeios: Viagens pontuais (até R$ 2.500), gastos recorrentes em shopping e praia

📈 Produtos Financeiros Disponíveis

    Tesouro Selic: Renda fixa, risco baixo, aporte mínimo R$ 30, indicado para reserva de emergência

    CDB Liquidez Diária: Renda fixa, risco baixo, aporte mínimo R$ 100, rendimento diário

    LCI/LCA: Renda fixa, risco baixo, aporte mínimo R$ 1.000, isento de IR, prazo mínimo 90 dias

    Fundos Imobiliários: Risco médio, rentabilidade 6–12% a.a., aporte entre R$ 10 e R$ 100, indicado para perfil moderado

    Fundos de Ações: Risco alto, rentabilidade variável, aporte mínimo R$ 100, indicado para perfil arrojado


...
```
