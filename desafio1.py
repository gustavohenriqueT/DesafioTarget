import json

with open("vendas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

comissoes = {}
detalhes = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if valor < 100:
        percentual = 0
    elif valor < 500:
        percentual = 0.01
    else:
        percentual = 0.05

    comissao = valor * percentual

    if vendedor not in comissoes:
        comissoes[vendedor] = 0
        detalhes[vendedor] = []

    comissoes[vendedor] += comissao

    detalhes[vendedor].append({
        "valor": valor,
        "percentual": percentual * 100,
        "comissao": comissao
    })

for vendedor in detalhes:
    print(f"\n{vendedor}")

    for venda in detalhes[vendedor]:
        print(f"Venda: R$ {venda['valor']:.2f} "
            f"| Comissão: {venda['percentual']:.0f}% "
            f"-> R$ {venda['comissao']:.2f}")


    print(f"TOTAL de comissão: R$ {comissoes[vendedor]:.2f}")
