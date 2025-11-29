DESAFIO TARGET - DOCUMENTAÇÃO

1. CÁLCULO DE COMISSÃO POR VENDEDOR

O programa lê um arquivo JSON contendo uma lista de vendas realizadas por vários vendedores.
Para cada venda individual, a comissão é calculada conforme as regras:

- Vendas abaixo de R$100,00 → 0% de comissão
- Vendas entre R$100,00 e R$499,99 → 1% de comissão
- Vendas a partir de R$500,00 → 5% de comissão

As comissões de cada venda são somadas e apresentadas como total do vendedor.

----------------------------------
JSON de entrada (vendas.json)
----------------------------------

{
  "vendas": [
    { "vendedor": "João Silva", "valor": 1200.50 },
    { "vendedor": "João Silva", "valor": 950.75 },
    { "vendedor": "João Silva", "valor": 1800.00 },
    { "vendedor": "João Silva", "valor": 1400.30 },
    { "vendedor": "João Silva", "valor": 1100.90 },
    { "vendedor": "João Silva", "valor": 1550.00 },
    { "vendedor": "João Silva", "valor": 1700.80 },
    { "vendedor": "João Silva", "valor": 250.30 },
    { "vendedor": "João Silva", "valor": 480.75 },
    { "vendedor": "João Silva", "valor": 320.40 },

    { "vendedor": "Maria Souza", "valor": 2100.40 },
    { "vendedor": "Maria Souza", "valor": 1350.60 },
    { "vendedor": "Maria Souza", "valor": 950.20 },
    { "vendedor": "Maria Souza", "valor": 1600.75 },
    { "vendedor": "Maria Souza", "valor": 1750.00 },
    { "vendedor": "Maria Souza", "valor": 1450.90 },
    { "vendedor": "Maria Souza", "valor": 400.50 },
    { "vendedor": "Maria Souza", "valor": 180.20 },
    { "vendedor": "Maria Souza", "valor": 90.75 },

    { "vendedor": "Carlos Oliveira", "valor": 800.50 },
    { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
    { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
    { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
    { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
    { "vendedor": "Carlos Oliveira", "valor": 300.40 },
    { "vendedor": "Carlos Oliveira", "valor": 500.00 },
    { "vendedor": "Carlos Oliveira", "valor": 125.75 },

    { "vendedor": "Ana Lima", "valor": 1000.00 },
    { "vendedor": "Ana Lima", "valor": 1100.50 },
    { "vendedor": "Ana Lima", "valor": 1250.75 },
    { "vendedor": "Ana Lima", "valor": 1400.20 },
    { "vendedor": "Ana Lima", "valor": 1550.90 },
    { "vendedor": "Ana Lima", "valor": 1650.00 },
    { "vendedor": "Ana Lima", "valor": 75.30 },
    { "vendedor": "Ana Lima", "valor": 420.90 },
    { "vendedor": "Ana Lima", "valor": 315.40 }
  ]
}

2. SISTEMA DE MOVIMENTAÇÃO DE ESTOQUE

O programa controla entradas e saídas de produtos do estoque, conforme o JSON inicial.

Cada movimentação contém:
- Um identificador único (UUID)
- Uma descrição da movimentação
- Quantidade movimentada
- Estoque final atualizado
- Registro completo em arquivo de log

----------------------------------
JSON de entrada (estoque.json)
----------------------------------

{
  "estoque": [
    {
      "codigoProduto": 101,
      "descricaoProduto": "Caneta Azul",
      "estoque": 150
    },
    {
      "codigoProduto": 102,
      "descricaoProduto": "Caderno Universitário",
      "estoque": 75
    },
    {
      "codigoProduto": 103,
      "descricaoProduto": "Borracha Branca",
      "estoque": 200
    },
    {
      "codigoProduto": 104,
      "descricaoProduto": "Lápis Preto HB",
      "estoque": 320
    },
    {
      "codigoProduto": 105,
      "descricaoProduto": "Marcador de Texto Amarelo",
      "esteque": 90
    }
  ]
}

3. CÁLCULO DE JUROS COM MULTA DIÁRIA DE 2,5%
   
O programa calcula:
- Dias de atraso
- Juros acumulados aplicando 2,5% ao dia
- Valor final atualizado
- ID único da operação
- Registro completo em arquivo .log

Fórmula utilizada:

valor_final = valor_original * (1 + 0.025) ^ dias_atraso

Exemplo:
- Valor original: R$1000
- Data de vencimento: 2025-01-10
- Dias em atraso: variável conforme data atual
- Multa: 2.5% ao dia

COMO EXECUTAR

1. Instale Python (versão 3.10+)
2. Clone o repositório:
   git clone https://github.com/SEU-USUARIO/DesafioTarget.git

3. Execute os scripts:
   python desafio1.py   → comissão de vendedores
   python desafio2.py    → movimentação de estoque
   python desafio3.py      → cálculo de juros


AUTOR


Gustavo Henrique Tomaz
