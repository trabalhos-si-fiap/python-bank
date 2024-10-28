from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
from datetime import datetime

from src.Enums.InvestEnum import InvestEnum
from src.myUtils import formata_brl


class Investimento:

    def __init__(self, aporte_inicial: float, taxa_contratada_aa: float, tipo: InvestEnum):
        self.data_aplicacao: datetime = datetime.now()
        self.aporte_inicial = Decimal(aporte_inicial)
        self.total_bruto = Decimal(aporte_inicial)
        self.total_liquido = Decimal(aporte_inicial)
        self.rendimento_total_bruto = 0
        self.rendimento_total_liquido = 0
        self.resgate = 0
        self.taxa_contratada_aa = taxa_contratada_aa
        self.taxa_contratada_ad = self.__yield_anual_para_diaria(taxa_contratada_aa)
        self.tabela_retorno = dict()
        self.proximo_dia_a_rentabilizar = 1
        self.tipo = tipo

    def __yield_anual_para_diaria(self, _yield: float) -> Decimal:
        return Decimal((1 + _yield) ** (1 / 365) - 1).quantize(Decimal('0.00001'), rounding=ROUND_DOWN)

    def get_dias_investidos(self) -> int:
        # Estou considerando segundos como dias para essa aplicação
        return int((datetime.now() - self.data_aplicacao).total_seconds())

    def resgatar_por_valor_bruto(self, valor_resgatado: float) -> Decimal:
        self.total_bruto -= Decimal(valor_resgatado)

        # calcular o ir
        rendimento_total = sum(map(lambda x: x[1], self.tabela_retorno.values()))
        ir = rendimento_total * (Decimal(valor_resgatado) / self.aporte_inicial) * self.get_taxa_imposto()

        return Decimal(valor_resgatado) - ir

    def processa_rentabilidade(self) -> None:

        for dia in range(self.proximo_dia_a_rentabilizar, self.get_dias_investidos() + 1):
            if dia in self.tabela_retorno.keys():
                print('pulando dia já rentabilizado.')
                continue

            rendimento_bruto = self.total_bruto * self.taxa_contratada_ad

            self.tabela_retorno[dia] = (
                Decimal(self.total_bruto).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                Decimal(rendimento_bruto).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            )

            self.total_bruto += rendimento_bruto

            self.proximo_dia_a_rentabilizar = dia + 1


    # Como calcular o rendimento bruto, rendimento líquido e i IR depois de um resgate?
    def get_rendimento_bruto(self) -> Decimal:
        self.rendimento_total_bruto = sum(map(lambda x: x[1], self.tabela_retorno.values()))
        return self.rendimento_total_bruto

    def get_rendimento_liquido(self) -> Decimal:

        self.rendimento_liquido = self.rendimento_total_bruto * Decimal(str(1 - self.get_taxa_imposto()))
        return self.rendimento_liquido

    def get_total_liquido(self) -> Decimal:
        self.total_liquido = self.total_bruto - Decimal(str(self.get_ir()))
        return self.total_liquido

    def get_ir(self) -> Decimal:
        return self.rendimento_total_bruto - self.rendimento_liquido

    def get_taxa_imposto(self) -> Decimal:
        if self.tipo.e_isento_de_ir():
            return Decimal(0)

        dias = self.get_dias_investidos()
        if dias <= 180:
            return Decimal(0.225)
        if dias <= 360:
            return Decimal(0.2)
        if dias <= 720:
            return Decimal(0.175)
        return Decimal(0.15)

    def get_texto_ir(self) -> str:
        tem_ir = f"Alíquota de IR {self.get_taxa_imposto() * 100:.2f}%\n"
        nao_tem_ir = "Investimento isento de IR\n"
        return tem_ir if self.get_taxa_imposto() > 0 else nao_tem_ir

    def __eq__(self, other):
        return self.total_bruto == other.total_bruto \
            and self.get_dias_investidos() == other.get_dias_investidos() \
            and self.tipo.name == other.tipo.name

    def __str__(self) -> str:
        self.processa_rentabilidade()
        return f"Nome: {self.tipo.name} \n" + \
            f"Aporte inicial: {formata_brl(self.aporte_inicial)} \n" + \
            f"Dias investidos {self.get_dias_investidos()} \n" + \
            f"Taxa contratada {self.taxa_contratada_aa * 100:.2f}% ao ano. \n" + \
            f"Taxa contratada {self.taxa_contratada_ad * 100:.4f}% ao dia. \n" + \
            f"Rendimento bruto {formata_brl(self.get_rendimento_bruto())} \n" + \
            f"Rendimento líquido {formata_brl(self.get_rendimento_liquido())} \n" + \
            f"Total bruto {formata_brl(self.total_bruto)} \n" + \
            f"Total líquido {formata_brl(self.get_total_liquido())} \n" + \
            f"Total IR {formata_brl(self.get_ir())} \n" + \
            self.get_texto_ir()
