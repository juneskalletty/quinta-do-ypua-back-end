from flask import Flask

from routes.reserva_api import cadastrar_reserva, consultar_reservas, editar_reserva, excluir_reserva
from routes.meuCaixa_api import cadastrar_pagamento, consultar_pagamentos, editar_pagamento, excluir_pagamento
from routes.usuarioAdmin_api import cadastrar_usuario, editar_usuario, excluir_usuario

app = Flask(__name__)

# Rotas reserva
app.add_url_rule('/cadastrar_reserva', view_func=cadastrar_reserva, methods=['POST'])
app.add_url_rule('/consultar_reservas', view_func=consultar_reservas, methods=['GET'])
app.add_url_rule('/editar_reserva', view_func=editar_reserva, methods=['PUT'])
app.add_url_rule('/excluir_reserva/<int:id_reserva>', view_func=excluir_reserva, methods=['DELETE'])

# Rotas Meu Caixa
app.add_url_rule('/cadastrar_pagamento', view_func=cadastrar_pagamento, methods=['POST'])
app.add_url_rule('/consultar_pagamentos', view_func=consultar_pagamentos, methods=['GET'])
app.add_url_rule('/editar_pagamento', view_func=editar_pagamento, methods=['PUT'])
app.add_url_rule('/excluir_pagamento/<int:id_pagamento>', view_func=excluir_pagamento, methods=['DELETE'])

# Rotas UsuarioAdmin
app.add_url_rule('/cadastrar_usuario', view_func=cadastrar_usuario, methods=['POST'])
app.add_url_rule('/editar_usuario', view_func=editar_usuario, methods=['PUT'])
app.add_url_rule('/excluir_usuario/<int:id_usuario>', view_func=excluir_usuario, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)

