from marshmallow import Schema, fields

class PagamentoSchema(Schema):
    fk_id_reserva = fields.Int(required=True)
    fk_valor_total = fields.Float(required=True)
    data_pagamento = fields.Date(required=True)
    #a variavel "pagamento_realizado" realmente não precisa estar aqui.
