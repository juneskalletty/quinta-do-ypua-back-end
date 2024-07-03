from marshmallow import Schema, fields

class ReservaSchema(Schema):
    nome_hospede = fields.Str(required=True)
    cpf_hospede = fields.Str(required=True)
    fone_hospede = fields.Str(required=True)
    data_nasc_hospede = fields.Date(required=True)
    quantidade_pessoas = fields.Int(required=True)
    forma_pagamento = fields.Str(required=True)
    servico_quarto = fields.Str(required=True)
    nome_acomodacao = fields.Str(required=True)
    tipo_acomodacao = fields.Str(required=True)
    valor_diaria = fields.Float(required=True)
    data_checkin = fields.Date(required=True)
    data_checkout = fields.Date(required=True)
    status = fields.Str(required=True)
    valor_total = fields.Float(required=True)
