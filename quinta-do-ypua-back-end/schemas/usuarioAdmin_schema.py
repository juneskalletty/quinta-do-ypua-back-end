from marshmallow import Schema, fields

class UsuarioSchema(Schema):
    id_usuario = fields.Int(required=False) 
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True)
