from src.Enums.AcaoEnum import Acao
from src.Enums.EmprestimoEnum import EmprestimoEnum
from src.Enums.InvestEnum import InvestEnum
from src.Models.Investimento import Investimento


class Menu:
    def __init__(self):
        ...

    def __cabecalho(self) -> str:
        texto = "* " * 10 + "\n"
        texto += "VIP BANK".center(20) + "\n"
        return texto

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
        texto = self.__cabecalho()
        texto += "Escolha uma opção:" + "\n"
        texto += "1 - Fazer investimento" + "\n"
        texto += "2 - Realizar resgate" + "\n"
        texto += "3 - Contratar um empréstimo" + "\n"
        texto += "4 - Sair" + "\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 1, 4)
        return Acao(int(escolha_validada))

    def investir(self) -> InvestEnum:
        texto = self.__cabecalho()
        texto += "Investimentos:" + "\n"
        texto += "Escolha uma opção:" + "\n"
        texto += f"1 - CDB Pré-Fixado {InvestEnum.CDB.get_taxa_contratada() * 100:.2f}% a.a. liquidez diária." + "\n"
        texto += f"2 - LCI Pré-Fixado {InvestEnum.LCI.get_taxa_contratada() * 100:.2f}% a.a. liquidez diária e isento de IR." + "\n"
        texto += f"3 - LCA Pré-Fixado {InvestEnum.LCA.get_taxa_contratada() * 100:.2f}% a.a. liquidez diária e isento de IR." + "\n"
        texto += "4 - Voltar." + "\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 1, 4)

        return InvestEnum(int(escolha_validada))

    def resgatar(self, investimentos: list[Investimento]) -> int | None:
        texto = self.__cabecalho()
        texto += "Você selecionou a opção resgate:\n"

        if len(investimentos) == 0:
            print(texto)
            print("Você não tem investimentos para resgatar.")
            print("* " * 10)
            return None

        for i, inv in enumerate(investimentos):
            print(f"{i + 1} - {inv}")

        print("Digite 0 para voltar e cancelar o resgate.")
        texto += f"Escolha um ativo a ser resgatado {1} a {len(investimentos)}:\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 0, len(investimentos))

        if escolha_validada == '0':
            print("Voltando...")
            return None

        return int(escolha_validada) - 1

    def emprestimo(self) -> EmprestimoEnum | None:
        texto = self.__cabecalho()
        texto += "Emprestimo selecionado." + "\n"
        texto += "Escolha uma opção:" + "\n"
        texto += "1 - R$ 1.000,00 em 5 parcelas com juros de 10% a.m." + "\n"
        texto += "2 - R$ 500,00 em 3 parcelas com juros de 10% a.m." + "\n"
        texto += "3 - R$ 300,00 em 2 parcelas com juros de 10% a.m." + "\n"
        texto += "4 - Montar proposta" + "\n"
        texto += "5 - Sair" + "\n"
        texto += "* " * 10 + "\n"

        escolha_validada = self.__validar(texto, self._validador_de_escolha, 1, 5)

        if escolha_validada == '5':
            print("Voltando...")
            return None

        return EmprestimoEnum(int(escolha_validada))
