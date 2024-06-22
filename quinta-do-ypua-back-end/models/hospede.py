class Hospede:
    def __init__(self, nome: str, cpf: int, fone: int, data_nasc: date, quantidade_pessoas: int, forma_pagamento: str, servico_quarto: bool):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.data_nasc = data_nasc
        self.quantidade_pessoas = quantidade_pessoas
        self.forma_pagamento = forma_pagamento
        self.servico_quarto = servico_quarto