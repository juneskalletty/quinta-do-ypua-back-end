class UsuarioAdmin:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha