from dataclasses import dataclass
from datetime import datetime

from src.InvestEnum import InvestEnum
from src.Menu import Menu


@dataclass
class Investimento:
    data: datetime
    valor: float
    tipo: InvestEnum


def formato_br_para_americano(valor) -> str:
    return valor.replace('.', '').replace(',', '.')


class InvestimentoService:
    def __init__(self, menu: Menu):
        self.menu = menu
        self.historico: list[Investimento] = []

    def imposto(self, dias: int) -> float:
        if dias <= 180:
            return 0.225
        if dias <= 360:
            return 0.2
        if dias <= 720:
            return 0.175
        return 0.15

    def mostrar_investimentos(self):
        print('Seus investimentos:\n')

        for item in self.historico:
            print(f'Tipo: {item.tipo.name}')
            print(f'Valor aplicado R$ {item.valor:,.2f}')
            print(f'Data: {item.data.strftime("%d/%m/%Y %H:%M:%S")}\n')

    def _depositar(self) -> float:
        while True:
            depoisto = input('Digite o valor que você deseja investir R$: ')

            try:
                depoisto = formato_br_para_americano(depoisto)
                return float(depoisto)
            except ValueError:
                print('Valor inválido, tente novamente.')

    def run(self) -> None:
        escolha = menu.investir()

        if escolha == escolha.VOLTAR:
            print('Voltando...')
            return None

        valor = self._depositar()
        self.historico.append(Investimento(datetime.now(), valor, escolha))

        print(f'Você investiu R$ {valor:,.2f} em {escolha.name}.')
        self.mostrar_investimentos()


class Resgate:
    def __init__(self, menu: Menu):
        self.menu = menu

    def run(self):
        menu.resgatar()


class Emprestimo:
    def __init__(self, menu: Menu):
        self.menu = menu

    def run(self):
        menu.emprestimo()


class Manager:
    def __init__(self, investir: InvestimentoService, resgatar: Resgate, emprestimo: Emprestimo):
        self.investir = investir
        self.resgatar = resgatar
        self.emprestimo = emprestimo

    def realizar_investimento(self):
        self.investir.run()

    def realizar_resgate(self):
        self.resgatar.run()

    def realizar_emprestimo(self):
        self.emprestimo.run()


if __name__ == '__main__':
    menu = Menu()
    manager = Manager(InvestimentoService(menu), Resgate(menu), Emprestimo(menu))
    while True:
        acao = menu.tela_inicial()
        acao.run(manager)
