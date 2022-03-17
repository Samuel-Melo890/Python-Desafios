print('='*8,'Lista de Cadastro de Clientes','='*8)
from module.interface import *
import sqlite3
from sqlite3 import Error
from time import sleep

conn = sqlite3.connect('C:\\Users\\saymu\\Desktop\\ExerciciosPYTHON\\NovPython\\Banco\\Cadastro.sqlite')
cursor = conn.cursor()

while True:
    menu('Cadastro de Clientes')
    print('> \033[36mOlá, seja bem vindo à loja do Seu Zé!\033[m')
    op = options('Cadastrar um novo cliente', 'Ver lista de clientes cadastrados','Modificar dados do cliente', 'SAir do programa')
    if op == 1 or op == 2 or op == 3:
        while True:
            try:
                if op == 1:
                    sleep(1.5)
                    titulo('Novo Cliente')
                    nome = str(input('Nome do cliente: ')).strip().title()
                    telefone = str(input('Telefone: ')).strip()
                    email = str(input('Email: ')).strip()
                    endereco = str(input('Endereço: ')).strip().title()
                    sleep(1)
                    cursor.execute(f'''INSERT INTO clientes2 (T_Nome, T_Telefone, T_Email, T_Endereco)
                                VALUES('{nome}', '{telefone}', '{email}', '{endereco}')''')
                    conn.commit()
                    print('\033[32mCadastro Realizado!\033[m')
                    sleep(1)
                elif op == 2:
                    sleep(1.5)
                    cursor.execute('SELECT * FROM clientes2')
                    lista_c = cursor.fetchall()
                    titulo('Lista de Clientes')
                    for cliente in lista_c:
                        print(f'Cliente \033[36m{cliente[1]}\033[m:')
                        print(f'    \033[35mID:\033[m {cliente[0]}')
                        print(f'    \033[35mNome:\033[m {cliente[1]}')
                        print(f'    \033[35mTelefone:\033[m {cliente[2]}')
                        print(f'    \033[35mEmail:\033[m {cliente[3]}')
                        print(f'    \033[35mEndereço:\033[m {cliente[4]}')
                        sleep(0.4)
                    if len(lista_c) == 0:
                        print('\033[36m>Lista de cadastros vazia\033[m')
                    sleep(1)
                else:
                    sleep(1.5)
                    id = int(input('Qual o ID da pessoa a ser modificada? '))
                    if id > len(lista_c) or id < 1:
                        print('\033[31mID inválido! Tente de novo!\033[m')
                        continue
                    novo_n = str(input('Novo nome: ')).strip().title()
                    novo_tel = str(input('Novo telefone: ')).strip()
                    novo_email = str(input('Novo email: ')).strip()
                    novo_end = str(input('Novo endereço: ')).strip().title()
                    sleep(1)
                    cursor.execute(f'UPDATE clientes2 SET T_Nome="{novo_n}" WHERE I_ID={id}')
                    cursor.execute(f'UPDATE clientes2 SET T_Telefone="{novo_tel}" WHERE I_ID={id}')
                    cursor.execute(f'UPDATE clientes2 SET T_Email="{novo_email}" WHERE I_ID={id}')
                    cursor.execute(f'UPDATE clientes2 SET T_Endereco="{novo_end}" WHERE I_ID={id}')
                    conn.commit()
                    print('\033[32mCadastro Atualizado!\033[m')
                    sleep(1)
            except (IndexError, KeyboardInterrupt, ValueError, TypeError):
                print('\033[31mERRO! Dado inválidos! Tente novamente:\033[m')
            else:
                break
    else:
        titulo('Saindo do Programa...')
        sleep(2)
        break
cursor.close()
conn.close()
print('\033[36mPrograma Finalizado!\033[m')
