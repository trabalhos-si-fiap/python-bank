from src.Enums.EmprestimoEnum import EmprestimoEnum
from src.Menu import Menu
from decimal import Decimal, ROUND_HALF_UP

from src.myUtils import formata_brl


class Emprestimo:
    def __init__(self, menu: Menu):
        self.menu = menu

    def calcular_pacelas(self, valor_emprestimo: Decimal, num_parcelas: int, taxa_mensal: Decimal) -> Decimal:
        if taxa_mensal == 0:
            parcela = valor_emprestimo / num_parcelas
        else:
            parcela = (valor_emprestimo * taxa_mensal) / (1 - (1 + taxa_mensal) ** -num_parcelas)

        return Decimal(parcela).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def run(self):
        emprestimo_enum = self.menu.emprestimo()

        if emprestimo_enum is None:
            return

        if emprestimo_enum.name == EmprestimoEnum.PROPOSTA_LIVRE.name:
            valor = self.pedir_valor()
            numero_parcelas = self.pedir_parcelas()
            # Verificar multiplo
        else:
            valor = emprestimo_enum.get_pacote()['valor']
            numero_parcelas = emprestimo_enum.get_pacote()['parcelas']

        juros_am = Decimal(emprestimo_enum.get_pacote()['juros_am'])
        parcelas = self.calcular_pacelas(valor, numero_parcelas, juros_am)

        print('Você escolheu empréstimo.')
        print('Pacote selecionado:')
        print(
            f'Valor: {formata_brl(valor)} | numero de parcelas: {numero_parcelas} | juros ao mes {juros_am * 100:.2f} %'
        )
        print(f'Valor das parcelas {formata_brl(parcelas)}')
        print(f'Total a pagar {formata_brl(parcelas * numero_parcelas)}')
        print(f'Total de juros {formata_brl(parcelas * numero_parcelas - valor)}')

    def pedir_valor(self) -> Decimal:
        while True:
            valor = input('Digite o valor do crédito desejado: R$ ')

            try:
                float(valor)
            except ValueError:
                print('Valor inválido, tente novamente.')
                continue

            if float(valor) < 0:
                print('Você não pode realizar empréstimos com valores negativos.')
                continue

            return Decimal(valor)

    def pedir_parcelas(self) -> int:
        while True:
            print('O prazo deve ser múltiplo de 2, 3 ou 5.')
            parcelas = input('Digite o prazo que você deseja pagar em meses: ')

            try:
                int(parcelas)
            except ValueError:
                print('Valor inválido, tente novamente.')
                continue

            parcelas = int(parcelas)

            if parcelas < 0:
                print('Valores negativos não são permitidos.')
                continue

            if parcelas % 2 != 0 and parcelas % 3 != 0 and parcelas % 5 != 0:
                print('As parcelas devem ser múltiplas de 2, 3 ou 5.')
                continue

            return parcelas
