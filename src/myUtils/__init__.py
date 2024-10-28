import locale
from decimal import Decimal


def formato_br_para_americano(valor) -> str:
    return valor.replace('.', '').replace(',', '.')


def formata_brl(valor: float | Decimal) -> str:
    return locale.currency(valor, grouping=True)


def valida_se_numerico(input_msg: str) -> float:
    while True:
        valor = input(input_msg)
        try:
            valor = formato_br_para_americano(valor)
            return float(valor)
        except ValueError:
            print('Valor inválido, tente novamente.')
