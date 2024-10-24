from enum import Enum


class Acao(Enum):
    INVESTIMENTO = 1
    RESGATE = 2
    EMPRESTIMO = 3
    SAIR = 4


def valida_opcao_selecionada(funcao_selecionada: str) -> bool:
    valido = True
    if not funcao_selecionada.isdecimal() or funcao_selecionada not in ['1', '2', '3', '4']:
        print("Por favor, digite um número válido.")
        valido = False
    return valido


def menu() -> Acao:
    texto = "* " * 10 + "\n"
    texto += "VIP BANK".center(20) + "\n"
    texto += "Escolha uma opção:" + "\n"
    texto += "1 - Fazer investimento" + "\n"
    texto += "2 - Realizar resgate" + "\n"
    texto += "3 - Contratar um empréstimo" + "\n"
    texto += "4 - Sair" + "\n"
    texto += "* " * 10 + "\n"

    while True:
        print(texto)
        funcao_selecionada = input('Escolha uma opção: ').strip()
        if valida_opcao_selecionada(funcao_selecionada):
            return Acao(int(funcao_selecionada))


if __name__ == '__main__':
    resultado = menu()
    print(resultado)
