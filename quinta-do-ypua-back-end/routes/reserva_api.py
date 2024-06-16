from flask import Flask, request, jsonify
from database import create_connection #conexão com database

import psycopg2

app = Flask(__name__)

@app.route('/cadastrar_reserva', methods=['POST'])
def cadastrarReserva():
    # obter dados do corpo (entiade) da requisição
    data = request.get_json()
    id_reserva = data['id_reserva']
    data_checkin = data['data_checkin']
    data_checkout = data['data_checkout']
    fk_cpf_hospede = data['fk_cpf_hospede']

    # conectar ao banco de dados e inserir os dados
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO reservas (id_reserva, data_checkin, data_checkout, fk_cpf_hospede)
    VALUES (%s, %s, %s, %s)
    """
    
    try:
        cursor.execute(query, (id_reserva, data_checkin, data_checkout, fk_cpf_hospede))
        conn.commit()
        return jsonify({"status": "success", "message": "Reserva cadastrada com sucesso"}), 201
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao cadastrar reserva"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/consultar_reservas', methods=['GET'])
def consultarReservas():
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM reservas"
    
    try:
        cursor.execute(query)
        reservas = cursor.fetchall()
        reservas_list = []
        for reserva in reservas:
            reservas_list.append({
                'id_reserva': reserva[0],
                'data_checkin': reserva[1],
                'data_checkout': reserva[2],
                'fk_cpf_hospede': reserva[3]
            })
        return jsonify(reservas_list), 200
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao consultar reservas"}), 500
    finally:
        cursor.close()
        conn.close()



@app.route('/editar_reserva', methods=['PUT'])
def editarReserva():

    data = request.get_json()
    id_reserva = data['id_reserva']
    data_checkin = data.get('data_checkin')
    data_checkout = data.get('data_checkout')
    fk_cpf_hospede = data.get('fk_cpf_hospede')

    conn = create_connection()
    cursor = conn.cursor()
    
    query = """
    UPDATE reservas
    SET data_checkin = %s, data_checkout = %s, fk_cpf_hospede = %s
    WHERE id_reserva = %s
    """
    
    try:
        cursor.execute(query, (data_checkin, data_checkout, fk_cpf_hospede, id_reserva))
        conn.commit()
        return jsonify({"status": "success", "message": "Reserva atualizada com sucesso"}), 200
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao atualizar reserva"}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/excluir_reserva', methods=['DELETE'])
def excluirReserva():
    # obter o ID da reserva do corpo da requisição
    data = request.get_json()
    id_reserva = data['id_reserva']
    
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """
    DELETE FROM reservas
    WHERE id_reserva = %s
    """
    
    try:
        cursor.execute(query, (id_reserva,))
        conn.commit()
        return jsonify({"status": "success", "message": "Reserva excluída com sucesso"}), 200
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao excluir reserva"}), 500
    finally:
        cursor.close()
        conn.close()
