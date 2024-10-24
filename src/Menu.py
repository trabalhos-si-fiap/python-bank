from src.AcaoEnum import Acao
from src.InvestEnum import InvestEnum


class Menu:
    def __init__(self):
        ...

    def _validador_de_escolha(self, funcao_selecionada: str, primeira: int, ultima: int) -> bool:
        valido = True

        escolhas_possiveis = [str(item) for item in range(primeira, ultima + 1)]

        if not funcao_selecionada.isdecimal() or funcao_selecionada not in escolhas_possiveis:
            print("Por favor, digite um número válido.")
            valido = False
        return valido

    def __validar(self, texto: str, funcao_validadora: callable, primeira: int, ultima: int) -> str:
        while True:
            print(texto)
            opcao_selecionada = input('Escolha uma opção: ').strip()
            if funcao_validadora(opcao_selecionada, primeira, ultima):
                return opcao_selecionada

    def tela_inicial(self) -> Acao:
        texto = "* " * 10 + "\n"
        texto += "VIP BANK".center(20) + "\n"
        texto += "Escolha uma opção:" + "\n"
        texto += "1 - Fazer investimento" + "\n"
        texto += "2 - Realizar resgate" + "\n"
        texto += "3 - Contratar um empréstimo" + "\n"
        texto += "4 - Sair" + "\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 1, 4)
        return Acao(int(escolha_validada))

    def investir(self) -> InvestEnum:
        texto = "* " * 10 + "\n"
        texto += "VIP BANK".center(20) + "\n"
        texto += "Investimentos:" + "\n"
        texto += "Escolha uma opção:" + "\n"
        texto += "1 - CDB" + "\n"
        texto += "2 - LCI" + "\n"
        texto += "3 - LCA" + "\n"
        texto += "4 - Voltar" + "\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 1, 4)

        return InvestEnum(int(escolha_validada))

    def resgatar(self):
        ...

    def emprestimo(self):
        ...
