from flask import Flask, make_response, jsonify, json, request
from bd import Livros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def save_books():
    with open('bd.py', 'w') as f:
        f.write('Livros = ')
        json.dump(Livros, f)

@app.route('/livros', methods=['GET'])
def get_livros():
        return make_response (
            jsonify(
                data=Livros
            )
        )

@app.route('/livros', methods=['POST'])
def create_book():
    livro = request.json
    Livros.append(livro)
    save_books()
    return livro

@app.route('/livros/<int:id_livro>', methods=['DELETE'])
def delete_book(id_livro):
    for livro in Livros:
        if livro['id'] == id_livro:
            Livros.remove(livro)
            save_books()
            return f'O livro {livro["titulo"]} foi excluído com sucesso!'
    return 'Livro não encontrado.'


app.run()