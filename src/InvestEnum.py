from enum import Enum


class InvestEnum(Enum):
    CDB = 1
    LCI = 2
    LCA = 3
    VOLTAR = 4

    def e_isento_de_ir(self) -> bool:
        if self.name == self.CDB:
            return False
        return True


