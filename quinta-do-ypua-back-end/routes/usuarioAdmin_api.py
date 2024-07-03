from flask import Flask, request, jsonify
from db.database import create_connection
from psycopg2 import DatabaseError
from models.usuarioAdmin import UsuarioAdmin
from schemas.usuarioAdmin_schema import UsuarioSchema

app = Flask(__name__)
usuario_schema = UsuarioSchema()

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    errors = usuario_schema.validate(dados)
    if errors:
        return jsonify({"status": "error", "message": errors}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO usuario (nome, email, senha)
    VALUES (%s, %s, %s)
    RETURNING id_usuario
    """

    try:
        cursor.execute(query, (
            dados["nome"], dados["email"], dados["senha"]
        ))
        id_usuario = cursor.fetchone()[0]
        conn.commit()
        return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso", "id_usuario": id_usuario}), 201
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao cadastrar usuário"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/editar_usuario', methods=['PUT'])
def editar_usuario():
    dados = request.get_json()
    errors = usuario_schema.validate(dados)
    if errors:
        return jsonify({"status": "error", "message": errors}), 400

    if not dados.get('id_usuario'):
        return jsonify({"status": "error", "message": "ID do usuário é obrigatório"}), 400

    conn = create_connection()
    cursor = conn.cursor()

    query = "UPDATE usuario SET "

    update_fields = []
    update_values = []
    for key, value in dados.items():
        if key != 'id_usuario':
            update_fields.append(f"{key} = %s")
            update_values.append(value)

    if not update_fields:
        return jsonify({"status": "error", "message": "Nenhum campo informado para atualização"}), 400

    query += ", ".join(update_fields) + " WHERE id_usuario = %s"
    update_values.append(dados.get('id_usuario'))

    try:
        cursor.execute(query, update_values)
        conn.commit()
        return jsonify({"status": "success", "message": "Usuário atualizado com sucesso"}), 200
    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao atualizar usuário"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/excluir_usuario/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    conn = create_connection()
    cursor = conn.cursor()

    query = "DELETE FROM usuario WHERE id_usuario = %s"

    try:
        cursor.execute(query, (id_usuario,))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"status": "success", "message": "Usuário excluído com sucesso"}), 200
        else:
            return jsonify({"status": "error", "message": "Usuário não encontrado"}), 404

    except (Exception, DatabaseError) as error:
        print(error)
        return jsonify({"status": "error", "message": "Erro ao excluir usuário"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
