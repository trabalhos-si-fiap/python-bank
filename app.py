from src.Menu import Menu
from src.services.EmprestimoService import Emprestimo
from src.services.InvestimentoService import InvestimentoService


class Manager:
    def __init__(self, investir: InvestimentoService, emprestimo: Emprestimo):
        self.investimentos_service = investir
        self.emprestimo = emprestimo

    def realizar_investimento(self):
        self.investimentos_service.investir()

    def realizar_resgate(self):
        self.investimentos_service.resgatar()

    def realizar_emprestimo(self):
        self.emprestimo.run()


if __name__ == '__main__':
    menu = Menu()
    invest_service = InvestimentoService(menu)

    manager = Manager(invest_service, Emprestimo(menu))
    while True:
        acao = menu.tela_inicial()
        acao.run(manager)
