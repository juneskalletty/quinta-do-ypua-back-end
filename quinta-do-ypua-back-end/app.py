from flask import Flask
# importa a função editaReserva do módulo api/routes.py
from routes.reserva_api.py import editarReserva
# importa a função cadastrarReserva do módulo api/routes.py
from routes.reserva_api import cadastrarReserva
# importa a função excluirReserva do módulo api/routes.py
from routes.reserva_api import excluirReserva
# importa a função consultarReserva do módulo api/routes.py
from routes.reserva_api import consultarReservas

app = Flask(__name__)

# registra a rota editarReserva com o app Flask
app.add_url_rule('/edita_reserva', view_func=editarReserva, methods=['PUT'])
app.add_url_rule('/cadastrar_reserva',
                 view_func=cadastrarReserva, methods=['POST'])
app.add_url_rule('/excluir_reserva',
                 view_func=excluirReserva, methods=['DELET'])
app.add_url_rule('/consultar_reserva',
                 view_func=cadastrarReserva, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
