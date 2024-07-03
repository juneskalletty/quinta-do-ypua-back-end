from flask import Flask, request, jsonify
from db.database import create_connection
from psycopg2 import DatabaseError
from models.pagamento import Pagamento
from schemas.pagamento_schema import PagamentoSchema

app = Flask(__name__)
pagamento_schema = PagamentoSchema()

@app.route('/cadastrar_pagamento', methods=['POST'])
def cadastrar_pagamento():
    dados = request.get_json()
    errors = pagamento_schema.validate(dados)
    if errors:
        return jsonify({"status": "error", "message": errors}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO pagamento (
        fk_id_reserva, fk_valor_total, data_pagamento, pagamento_realizado
    )
    VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (
            dados["fk_id_reserva"], dados["fk_valor_total"],
            dados["data_pagamento"], dados["pagamento_realizado"]
        ))
        conn.commit()
        return jsonify({"status": "success", "message": "Pagamento registrado com sucesso"}), 201
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao registrar pagamento"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/consultar_pagamentos', methods=['GET'])
def consultar_pagamentos():
    conn = create_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM pagamento"

    try:
        cursor.execute(query)
        pagamentos = cursor.fetchall()

        pagamentos_list = []
        for pagamento in pagamentos:
            pagamentos_list.append({
                'id_pagamento': pagamento[0],
                'fk_id_reserva': pagamento[1],
                'fk_valor_total': pagamento[2],
                'data_pagamento': pagamento[3],
                'pagamento_realizado': pagamento[4]
            })

        return jsonify(pagamentos_list), 200

    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao consultar pagamentos"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/editar_pagamento', methods=['PUT'])
def editar_pagamento():
    dados = request.get_json()

    if not dados.get('id_pagamento'):
        return jsonify({"status": "error", "message": "Dados inválidos"}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = "UPDATE pagamento SET "

    update_fields = []
    update_values = []
    for key, value in dados.items():
        if key != 'id_pagamento':
            update_fields.append(f"{key} = %s")
            update_values.append(value)

    if not update_fields:
        return jsonify({"status": "error", "message": "Nenhum campo informado para atualização"}), 400

    query += ", ".join(update_fields) + " WHERE id_pagamento = %s"
    update_values.append(dados.get('id_pagamento'))

    try:
        cursor.execute(query, update_values)
        conn.commit()
        return jsonify({"status": "success", "message": "Pagamento atualizado com sucesso"}), 200
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao atualizar pagamento"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/excluir_pagamento/<int:id_pagamento>', methods=['DELETE'])
def excluir_pagamento(id_pagamento):
    conn = create_connection()
    cursor = conn.cursor()

    query = "DELETE FROM pagamento WHERE id_pagamento = %s"

    try:
        cursor.execute(query, (id_pagamento,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"status": "success", "message": "Pagamento excluído com sucesso"}), 200
        else:
            return jsonify({"status": "error", "message": "Pagamento não encontrado"}), 404

    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao excluir pagamento"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
