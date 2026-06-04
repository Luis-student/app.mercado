import mysql.connector
from flask import Flask, jsonify, request
app =(__name__)

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
def cadastro():
    nome_produto = input("ensira o nome do produto : ")
    valor_produto = float(input("ensira o valor do produto : "))
    variacao = input("variação do produto : ")

    cursor.execute(f"INSERT INTO produtos (nome_produto, valor_produto, variacao) VALUES ('{nome_produto}', {valor_produto}, '{variacao}')")
    banco.commit()

    print("produto cadastrado com sucesso! ")

# listar produtos 
def listar():
    cursor.execute('SELECT * FROM produtos ')
    produtos  = cursor.fetchall()

    for produtos in produtos :
        print(produtos) 

# buscar produtos 
def buscar():
    termo = input("nome do produto : ")
    cursor.execute(f"SELECT * FROM produtos WHERE nome_produto LIKE ('{termo}')")

    produtos = cursor.fetchall()
    
    if produtos:
        for busca in produtos:
            print(busca)
    else:
        print('protudo não encontrado! ')

# Excluir produtos (DELETE)
def excluir():
    deletar = int(input('ID do produto: '))

    cursor.execute("" \
    "DELETE FROM produtos WHERE id_produto = %s",
    (deletar,)
    )

    banco.commit()

    if cursor.rowcount > 0:
        print('Produto excluído com sucesso!')
    else:
        print('Produto não encontrado.')

