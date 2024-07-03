from flask import Flask, request, jsonify
from db.database import create_connection
from psycopg2 import DatabaseError
from models.reserva import Reserva
from schemas.reserva_schema import ReservaSchema

app = Flask(__name__)
reserva_schema = ReservaSchema()

@app.route('/cadastrar_reserva', methods=['POST'])
def cadastrar_reserva():
    dados = request.get_json()
    errors = reserva_schema.validate(dados)
    if errors:
        return jsonify({"status": "error", "message": errors}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO reserva (
        nome_hospede, cpf_hospede, fone_hospede, data_nasc_hospede,
        quantidade_pessoas, forma_pagamento, servico_quarto, fk_id_acomodacao, valor_diaria, data_checkin, data_checkout, status, valor_total
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (
            dados["nome_hospede"], dados["cpf_hospede"], dados["fone_hospede"], dados["data_nasc_hospede"],
            dados["quantidade_pessoas"], dados["forma_pagamento"], dados["servico_quarto"], dados["fk_id_acomodacao"], dados["valor_diaria"], dados["data_checkin"], dados["data_checkout"],
            dados["status"], dados["valor_total"]
        ))
        conn.commit()
        return jsonify({"status": "success", "message": "Reserva cadastrada com sucesso"}), 201
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao cadastrar reserva"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/consultar_reservas', methods=['GET'])
def consultar_reservas():
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM reserva"

    try:
        cursor.execute(query)
        reservas = cursor.fetchall()

        reservas_list = []
        for reserva in reservas:
            reservas_list.append({
                'id_reserva': reserva[0],
                'nome_hospede': reserva[1],
                'cpf_hospede': reserva[2],
                'fone_hospede': reserva[3],
                'data_nasc_hospede': reserva[4],
                'quantidade_pessoas': reserva[5],
                'forma_pagamento': reserva[6],
                'servico_quarto': reserva[7],
                'fk_id_acomodacao': reserva[8],
                'valor_diaria': reserva[9],
                'data_checkin': reserva[10],
                'data_checkout': reserva[11],
                'status': reserva[12],
                'valor_total': reserva[13]
            })

        return jsonify(reservas_list), 200

    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao consultar reservas"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/editar_reserva', methods=['PUT'])
def editar_reserva():
    dados = request.get_json()

    if not dados.get('id_reserva') or not dados.get('data_checkin') or not dados.get('data_checkout'):
        return jsonify({"status": "error", "message": "Dados inválidos"}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = "UPDATE reserva SET "

    update_fields = []
    update_values = []
    for key, value in dados.items():
        if key != 'id_reserva':
            update_fields.append(f"{key} = %s")
            update_values.append(value)

    if not update_fields:
        return jsonify({"status": "error", "message": "Nenhum campo informado para atualização"}), 400

    query += ", ".join(update_fields) + " WHERE id_reserva = %s"
    update_values.append(dados.get('id_reserva'))

    try:
        cursor.execute(query, update_values)
        conn.commit()
        return jsonify({"status": "success", "message": "Reserva atualizada com sucesso"}), 200
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao atualizar reserva"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/excluir_reserva/<int:id_reserva>', methods=['DELETE'])
def excluir_reserva(id_reserva):
    conn = create_connection()
    cursor = conn.cursor()

    query = "DELETE FROM reserva WHERE id_reserva = %s"

    try:
        cursor.execute(query, (id_reserva,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"status": "success", "message": "Reserva excluída com sucesso"}), 200
        else:
            return jsonify({"status": "error", "message": "Reserva não encontrada"}), 404

    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao excluir reserva"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
