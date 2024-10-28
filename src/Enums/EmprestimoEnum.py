from enum import Enum


class EmprestimoEnum(Enum):
    MIL_REAIS = 1
    QUINHENTOS_REAIS = 2
    TRESENTOS_REAIS = 3
    PROPOSTA_LIVRE = 4

    def get_pacote(self):
        dict_ = {
            1: {
                'valor': 1000,
                'parcelas': 5,
                'juros_am': 0.1
            },
            2: {
                'valor': 500,
                'parcelas': 3,
                'juros_am': 0.1
            },
            3: {
                'valor': 300,
                'parcelas': 2,
                'juros_am': 0.1
            },
            4: {
                'valor': 'a definir',
                'parcelas': 'a definir',
                'juros_am': 0.1
            },
        }

        return dict_[self.value]
