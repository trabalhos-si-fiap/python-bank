from decimal import Decimal, ROUND_HALF_UP
from src.Menu import Menu
from src.Models.Investimento import Investimento
from src.myUtils import valida_se_numerico, formata_brl


class InvestimentoService:
    def __init__(self, menu: Menu):
        self.menu = menu
        self.investimentos: list[Investimento] = []

    def mostrar_investimentos(self):
        print('Seus investimentos:')
        for i, investimento in enumerate(self.investimentos):
            print(f'\n{i + 1} {investimento}')

    def investir(self) -> None:
        escolha = self.menu.investir()

        if escolha == escolha.VOLTAR:
            print('Voltando...')
            return None

        valor = valida_se_numerico('Digite o valor que você deseja investir R$: ')
        self.investimentos.append(Investimento(valor, escolha.get_taxa_contratada(), escolha))

        print(f'Você investiu R$ {valor:,.2f} em {escolha.name}.')
        self.mostrar_investimentos()

    def get_investments(self):
        return self.investimentos

    def resgatar(self):
        investimento_escolhido = self.menu.resgatar(self.investimentos)

        if investimento_escolhido is None:
            return

        investimento = self.investimentos[investimento_escolhido]

        while True:
            print(f'{investimento_escolhido + 1} {investimento.tipo.name} selecionado.')
            print(f'Você pode resgatar o valor máximo de {formata_brl(investimento.total_bruto)}')
            valor = valida_se_numerico('Digite o valor que deseja resgatar: R$ ')

            if Decimal(valor) > investimento.total_bruto:
                texto = f"Você não pode resgatar {formata_brl(valor)} pois é maior do que" + \
                        f"o saldo investido de {formata_brl(investimento.total_bruto)}."
                print(texto)
                continue

            if valor < 0:
                print('Você não pode resgatar valores negativos.\n')
                continue

            valor_resgatado_liquido = investimento.resgatar_por_valor_bruto(valor)

            print(
                f'Você resgatou {formata_brl(valor)}.\n' + \
                f'IR: {formata_brl(valor - float(valor_resgatado_liquido))}\n' + \
                f'Total líquido: {formata_brl(float(valor_resgatado_liquido))}'
            )

            if investimento.total_bruto.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP) == 0:
                self.investimentos.remove(investimento)
            break
