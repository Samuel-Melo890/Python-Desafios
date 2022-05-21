print('='*8,'Clientes Banco','='*8)
from module.bancodado import *
from module.interface import *
import sqlite3
from sqlite3 import Error
from time import sleep

conn = sqlite3.connect(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\Banco\Clientes.sqlite')
cursor = conn.cursor()

titulo('Lista de Clientes')
s = 'SELECT * FROM clientes'
cliente = cursor.execute(s).fetchall()
for id, n, i, e, cep in cliente:
    print(f'Cliente \033[36m{n}\033[m:')
    print(f' \033[35mID:\033[m {id}')
    print(f' \033[35mNome:\033[m {n}')
    print(f' \033[35mIdade:\033[m {i} anos')
    print(f' \033[35mEndereço:\033[m {e}')
    print(f' \033[35mCEP:\033[m {cep}\n')
    sleep(0.6)
if len(cliente) == 0:
    print('Lista vazia')
sleep(1.5)

while True:
    menu('Cadastro de Clientes')
    try:
        r = ' '
        while r not in 'SN':
            r = str(input('Deseja adicionar um novo cliente à lista? [S/N] ')).strip().upper()[0]
        if r in 'N':
            break
    except (IndexError, KeyboardInterrupt):
        print('\033[31mERRO! Por favor preencha os campos corretamente!\033[m')
    else:
        titulo('Novo Cliente')
        while True:
            try:
                nome = str(input('Nome: ')).strip().title()
                idade = int(input('Idade: '))
                endereço = str(input('Endereço: ')).strip().title()
                cep = str(input('CEP: '))
            except (IndexError, ValueError, TypeError, KeyboardInterrupt):
                print('\033[31mERRO! Preencha os dados corretamente!\033[m')
            else:
                nc = f'''INSERT INTO 
                    clientes(T_Nome, I_Idade, T_Endereco, T_CEP) 
                    VALUES('{nome}', '{idade}', '{endereço}', '{cep}')'''
                cursor.execute(nc)
                conn.commit()
                print('\033[32mCadastro Realizado!\033[m')
                sleep(1.5)
                break
cursor.close()
conn.close()
print('\033[36mPrograma Finalizado!\033[m')
