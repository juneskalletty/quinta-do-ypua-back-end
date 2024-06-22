class Reserva:
    def __init__(self, id_reserva: int, data_checkin: date, data_checkout: date, fk_cpf_hospede: int):
        self.id_reserva = id_reserva
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.fk_cpf_hospede = fk_cpf_hospede
