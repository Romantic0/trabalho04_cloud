import os
import json
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Caminho absoluto/relativo seguro para ler o JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'produtos.json')


def carregar_produtos():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Marketplace do Trabalho Final",
        "versao": "1.0.0",
        "status": "UP"
    }), 200


@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = carregar_produtos()
    return jsonify(produtos), 200


@app.route('/produtos/<int:produto_id>', methods=['GET'])
def get_produto_por_id(produto_id):
    produtos = carregar_produtos()
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto is None:
        abort(404)
    return jsonify(produto), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
