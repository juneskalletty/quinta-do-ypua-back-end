from datetime import date

class Reserva:
    def __init__(self, 
                 id_reserva: int, 
                 nome_hospede: str, 
                 cpf_hospede: str, 
                 fone_hospede: str, 
                 data_nasc_hospede: date,
                 quantidade_pessoas: int,
                 forma_pagamento: str,
                 servico_quarto: str,
                 fk_id_acomodacao: int,
                 valor_diaria: float,
                 data_checkin: date,
                 data_checkout: date,
                 status: str,
                 valor_total: float):
        self.id_reserva = id_reserva
        self.nome_hospede = nome_hospede
        self.cpf_hospede = cpf_hospede
        self.fone_hospede = fone_hospede
        self.data_nasc_hospede = data_nasc_hospede
        self.quantidade_pessoas = quantidade_pessoas
        self.forma_pagamento = forma_pagamento
        self.servico_quarto = servico_quarto
        self.fk_id_acomodacao = fk_id_acomodacao
        self.valor_diaria = valor_diaria
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = status
        self.valor_total = valor_total
