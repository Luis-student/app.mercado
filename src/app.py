import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

banco = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Jayme-123"
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS supermercado")
cursor.execute("USE supermercado")


# cadastro de produtos 
@app.route('/cadastro', methods=['POST'])
def cadastro():

    dados = request.get_json()

    nome_produto = dados['nome_produto']
    valor_produto = dados['valor_produto']
    variacao = dados['variacao']

    cursor.execute(f"INSERT INTO produtos (nome_produto, valor_produto, variacao) VALUES ('{nome_produto}', {valor_produto}, '{variacao}')")
    banco.commit()

    return jsonify({"message": 'produto cadastrado com sucesso! '})

# listar produtos     
@app.route('/listar', methods=['GET'])
def listar():
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    return jsonify(produtos)

# buscar produtos 
@app.route('/buscar', methods=['GET'])
def buscar():

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    return jsonify(produtos)

# Excluir produtos 
@app.route ('/excluir/<id_produto>', methods=['DELETE'])
def excluir(id_produto):    

    cursor.execute("" \
    "DELETE FROM produtos WHERE id_produto = %s",
    (id_produto,)
    )

    banco.commit()

    return jsonify('produto excluido !')

app.run()

