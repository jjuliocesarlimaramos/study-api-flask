from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Simulando um banco de dados com uma lista
usuarios = []

# Página inicial com lista de usuários
@app.route('/')
def index():
    return render_template_string('''
        <h1>Lista de Usuários</h1>
        <a href="{{ url_for('form_criar') }}">Adicionar Novo Usuário</a>
        <ul>
        {% for u in usuarios %}
            <li>
                {{ u['nome'] }} ({{ u['email'] }})
                [<a href="{{ url_for('form_editar', id_usuario=u['id']) }}">Editar</a>]
                [<a href="{{ url_for('deletar_usuario_web', id_usuario=u['id']) }}">Excluir</a>]
            </li>
        {% endfor %}
        </ul>
    ''', usuarios=usuarios)

# Formulário para criar usuário
@app.route('/novo', methods=['GET'])
def form_criar():
    return render_template_string('''
        <h2>Novo Usuário</h2>
        <form method="post" action="{{ url_for('criar_usuario_web') }}">
            Nome: <input type="text" name="nome"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit" value="Criar">
        </form>
        <a href="{{ url_for('index') }}">Voltar</a>
    ''')

# Criar usuário via formulário
@app.route('/novo', methods=['POST'])
def criar_usuario_web():
    nome = request.form['nome']
    email = request.form['email']
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "email": email
    }
    usuarios.append(novo_usuario)
    return redirect(url_for('index'))

# Formulário para editar usuário
@app.route('/editar/<int:id_usuario>', methods=['GET'])
def form_editar(id_usuario):
    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
    if not usuario:
        return "Usuário não encontrado", 404
    return render_template_string('''
        <h2>Editar Usuário</h2>
        <form method="post" action="{{ url_for('editar_usuario_web', id_usuario=usuario['id']) }}">
            Nome: <input type="text" name="nome" value="{{ usuario['nome'] }}"><br>
            Email: <input type="email" name="email" value="{{ usuario['email'] }}"><br>
            <input type="submit" value="Atualizar">
        </form>
        <a href="{{ url_for('index') }}">Voltar</a>
    ''', usuario=usuario)

# Atualizar usuário via formulário
@app.route('/editar/<int:id_usuario>', methods=['POST'])
def editar_usuario_web(id_usuario):
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuario['nome'] = request.form['nome']
            usuario['email'] = request.form['email']
            break
    return redirect(url_for('index'))

# Deletar usuário via link
@app.route('/excluir/<int:id_usuario>')
def deletar_usuario_web(id_usuario):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id_usuario]
    return redirect(url_for('index'))

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
    
