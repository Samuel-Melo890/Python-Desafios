import sqlite3
from sqlite3 import Error

def ConexaoBanco(str):
    caminho = str
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    else:
        return con


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as erro:
        print(f'\033[31m{erro}\033[m')
    else:
        c.close()
        print('\033[32mRegistro Inserido!\033[m')


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as erro:
        print(f'\033[31m{erro}\033[m')
    else:
        c.close()
        print('\033[31mRegistro Removido!\033[m')


def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as erro:
        print(f'\033[31m{erro}\033[m')
    else:
        c.close()
        print('\033[36mRegistro Atualizado!\033[m')


def consulta(conexao, sql):
    c = conexao.cursor()
    resultado = c.execute(sql).fetchall()
    c.close()
    return resultado
