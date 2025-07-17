from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um banco de dados com uma lista
usuarios = []

# CREATE
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados['nome'],
        "email": dados['email']
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# READ
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

# UPDATE
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    dados = request.get_json()
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# DELETE
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id_usuario]
    return jsonify({"mensagem": "Usuário deletado com sucesso"})

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
