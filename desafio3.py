from datetime import datetime
import uuid


def registrar_log(texto):
    with open("juros.log", "a", encoding="utf-8") as log:
        log.write(texto + "\n")


def calcular_juros(valor_original: float, data_vencimento: str, multa_dia: float = 0.025):
    """
    Calcula juros por atraso com multa diária.
    valor_original -> valor base
    data_vencimento -> string formato YYYY-MM-DD
    multa_dia -> percentual em decimal (0.025 = 2,5%)
    """

    try:
        venc = datetime.strptime(data_vencimento, "%Y-%m-%d").date()
    except ValueError:
        raise Exception("ERRO: Data de vencimento inválida. Use o formato YYYY-MM-DD.")

    hoje = datetime.now().date()
    dias_atraso = (hoje - venc).days

    if dias_atraso <= 0:
        dias_atraso = 0
        valor_final = valor_original
        juros = 0
    else:
        valor_final = valor_original * ((1 + multa_dia) ** dias_atraso)
        juros = valor_final - valor_original

    operacao_id = str(uuid.uuid4())

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_texto = (
        f"[{timestamp}] OP_ID={operacao_id} | VALOR_ORIG={valor_original} | "
        f"VENC='{data_vencimento}' | DIAS_ATRASO={dias_atraso} | MULTA_DIA={multa_dia} "
        f"| JUROS={juros:.2f} | VALOR_FINAL={valor_final:.2f}"
    )

    registrar_log(log_texto)

    return {
        "operacao_id": operacao_id,
        "valor_original": valor_original,
        "data_vencimento": data_vencimento,
        "dias_atraso": dias_atraso,
        "multa_dia": multa_dia,
        "juros": juros,
        "valor_final": valor_final
    }

if __name__ == "__main__":
    retorno = calcular_juros(1000, "2025-01-10")
    
    print("\nRELATÓRIO TÉCNICO DE JUROS")
    print(f"ID da Operação    : {retorno['operacao_id']}")
    print(f"Valor Original    : R$ {retorno['valor_original']:.2f}")
    print(f"Data de Vencimento: {retorno['data_vencimento']}")
    print(f"Dias em Atraso    : {retorno['dias_atraso']}")
    print(f"Multa ao Dia      : {retorno['multa_dia'] * 100:.2f}%")
    print(f"Juros Calculados  : R$ {retorno['juros']:.2f}")
    print(f"Valor Final       : R$ {retorno['valor_final']:.2f}")
