from src.Menu import Menu
from src.services.EmprestimoService import Emprestimo
from src.services.InvestimentoService import InvestimentoService
from src.services.Manager import Manager


class App:
    def __init__(self):
        menu = Menu()
        invest_service = InvestimentoService(menu)

        manager = Manager(invest_service, Emprestimo(menu))
        while True:
            acao = menu.tela_inicial()
            acao.run(manager)


