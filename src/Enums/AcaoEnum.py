import sys
from enum import Enum


class Acao(Enum):
    INVESTIMENTO = 1
    RESGATE = 2
    EMPRESTIMO = 3
    SAIR = 4

    def run(self, manager):
        if self == Acao.INVESTIMENTO:
            manager.realizar_investimento()
        elif self == Acao.RESGATE:
            manager.realizar_resgate()
        elif self == Acao.EMPRESTIMO:
            manager.realizar_emprestimo()
        elif self == Acao.SAIR:
            sys.exit()
