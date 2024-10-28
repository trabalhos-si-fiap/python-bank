from enum import Enum

# CDI_ANO = 10.75
CDI_ANO = 0.1


class InvestEnum(Enum):
    CDB = 1
    LCI = 2
    LCA = 3
    VOLTAR = 4

    def e_isento_de_ir(self) -> bool:
        if self.name == self.CDB.name:
            return False
        return True

    def get_taxa_contratada(self):
        taxa = {
            "CDB": CDI_ANO,
            "LCI": CDI_ANO * 0.8,
            "LCA": CDI_ANO * 0.85
        }
        return taxa[self.name]
