import json
import uuid
from datetime import datetime

def carregar_estoque():
    with open("estoque.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_estoque(dados):
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def registrar_log(movimento):
    with open("movimentacoes.log", "a", encoding="utf-8") as log:
        log.write(movimento + "\n")

def movimentar_estoque(codigo, quantidade, descricao):
    dados = carregar_estoque()
    produtos = dados["estoque"]

    for produto in produtos:
        if produto["codigoProduto"] == codigo:

            movimento_id = str(uuid.uuid4())

            estoque_anterior = produto["estoque"]
            estoque_final = estoque_anterior + quantidade
            produto["estoque"] = estoque_final

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_texto = (
                f"[{timestamp}] MOV_ID={movimento_id} | PROD={codigo} | DESC='{descricao}' | "
                f"QTD={quantidade} | ESTOQUE_ANT={estoque_anterior} | ESTOQUE_FINAL={estoque_final}"
            )

            registrar_log(log_texto)
            salvar_estoque(dados)

            print("\nMOVIMENTAÇÃO REGISTRADA")
            print(f"ID da Movimentação : {movimento_id}")
            print(f"Produto            : {produto['descricaoProduto']} ({codigo})")
            print(f"Quantidade Mov.    : {quantidade}")
            print(f"Estoque Anterior   : {estoque_anterior}")
            print(f"Estoque Atual      : {estoque_final}")
            print(f"Descrição Técnica  : {descricao}")
            print("\n")

            return

    print("ERRO: Código de produto não encontrado.")

movimentar_estoque(101, +20, "Entrada Nota Fiscal 1234")
movimentar_estoque(103, -15, "Saída para expedição 5678")
