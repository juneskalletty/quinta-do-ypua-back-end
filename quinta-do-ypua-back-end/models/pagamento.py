from datetime import date

class Pagamento:
    def __init__(self,
                 fk_id_reserva: int,
                 fk_valor_total: float,
                 data_pagamento: date,
                 pagamento_realizado: bool):
        self.fk_id_reserva = fk_id_reserva
        self.fk_valor_total = fk_valor_total
        self.data_pagamento = data_pagamento
        self.pagamento_realizado = pagamento_realizado