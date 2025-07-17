{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": "from flask import Flask, request, jsonify"
                },
                {
                    "line_number": 2,
                    "text": ""
                },
                {
                    "line_number": 3,
                    "text": "app = Flask(__name__)"
                },
                {
                    "line_number": 4,
                    "text": ""
                },
                {
                    "line_number": 5,
                    "text": "# Simulando um banco de dados com uma lista"
                },
                {
                    "line_number": 6,
                    "text": "usuarios = []"
                },
                {
                    "line_number": 7,
                    "text": ""
                },
                {
                    "line_number": 8,
                    "text": "# CREATE"
                },
                {
                    "line_number": 9,
                    "text": "@app.route('/usuarios', methods=['POST'])"
                },
                {
                    "line_number": 10,
                    "text": "def criar_usuario():"
                },
                {
                    "line_number": 11,
                    "text": "dados = request.get_json()"
                },
                {
                    "line_number": 12,
                    "text": "novo_usuario = {"
                },
                {
                    "line_number": 13,
                    "text": "\"id\": len(usuarios) + 1,"
                },
                {
                    "line_number": 14,
                    "text": "\"nome\": dados['nome'],"
                },
                {
                    "line_number": 15,
                    "text": "\"email\": dados['email']"
                },
                {
                    "line_number": 16,
                    "text": "}"
                },
                {
                    "line_number": 17,
                    "text": "usuarios.append(novo_usuario)"
                },
                {
                    "line_number": 18,
                    "text": "return jsonify(novo_usuario), 201"
                },
                {
                    "line_number": 19,
                    "text": ""
                },
                {
                    "line_number": 20,
                    "text": "# READ"
                },
                {
                    "line_number": 21,
                    "text": "@app.route('/usuarios', methods=['GET'])"
                },
                {
                    "line_number": 22,
                    "text": "def listar_usuarios():"
                },
                {
                    "line_number": 23,
                    "text": "return jsonify(usuarios)"
                },
                {
                    "line_number": 24,
                    "text": ""
                },
                {
                    "line_number": 25,
                    "text": "# UPDATE"
                },
                {
                    "line_number": 26,
                    "text": "@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])"
                },
                {
                    "line_number": 27,
                    "text": "def atualizar_usuario(id_usuario):"
                },
                {
                    "line_number": 28,
                    "text": "dados = request.get_json()"
                },
                {
                    "line_number": 29,
                    "text": "for usuario in usuarios:"
                },
                {
                    "line_number": 30,
                    "text": "if usuario['id'] == id_usuario:"
                },
                {
                    "line_number": 31,
                    "text": "usuario['nome'] = dados.get('nome', usuario['nome'])"
                },
                {
                    "line_number": 32,
                    "text": "usuario['email'] = dados.get('email', usuario['email'])"
                },
                {
                    "line_number": 33,
                    "text": "return jsonify(usuario)"
                },
                {
                    "line_number": 34,
                    "text": "return jsonify({\"erro\": \"Usu\u00e1rio n\u00e3o encontrado\"}), 404"
                },
                {
                    "line_number": 35,
                    "text": ""
                },
                {
                    "line_number": 36,
                    "text": "# DELETE"
                },
                {
                    "line_number": 37,
                    "text": "@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])"
                },
                {
                    "line_number": 38,
                    "text": "def deletar_usuario(id_usuario):"
                },
                {
                    "line_number": 39,
                    "text": "global usuarios"
                },
                {
                    "line_number": 40,
                    "text": "usuarios = [u for u in usuarios if u['id'] != id_usuario]"
                },
                {
                    "line_number": 41,
                    "text": "return jsonify({\"mensagem\": \"Usu\u00e1rio deletado com sucesso\"})"
                },
                {
                    "line_number": 42,
                    "text": ""
                },
                {
                    "line_number": 43,
                    "text": "# Iniciar o servidor"
                },
                {
                    "line_number": 44,
                    "text": "if __name__ == '__main__':"
                },
                {
                    "line_number": 45,
                    "text": "app.run(debug=True)"
                }
            ],
            "token_count": 166
        }
    ]
}