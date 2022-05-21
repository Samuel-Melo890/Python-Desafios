from module.interface import *
import sqlite3
from sqlite3 import Error
from time import sleep
import os

os.system('cls')

print('='*8,'Agenda no Python','='*8)

conn = sqlite3.connect(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\Banco\Agenda.sqlite')
cursor = conn.cursor()

while True:
    menu('Agenda de Cadastros Python')
    op = options('Inserir Cadastro', 'Deletar Cadastro', 'Atualizar Cadastro', 'Consultar Agenda','Consultar ID', 'Consultar Nome', 'Sair do Programa')
    
    if 1 <= op <= 6:
        while True:
            tabela = cursor.execute('SELECT * FROM agenda').fetchall()
            try:
                sleep(1)
                
                if op == 1:
                    titulo('Novo Cadastro')
                    nome = str(input('Nome: ')).strip().title()
                    telefone = str(input('Telefone: ')).strip()
                    email = str(input('Email: ')).strip()
                    
                    cursor.execute(f'''INSERT INTO agenda(T_Nome, T_Telefone, T_Email)
                                VALUES('{nome}', '{telefone}', '{email}')''')
                    conn.commit()
                    
                    sleep(1)
                    print('\033[32mCadastro Realizado!\033[m')
                    sleep(1)
                
                elif op == 2:
                    if len(tabela) == 0:
                        print('>\033[34mAgenda vazia.\033[m')
                        sleep(1)
                        break
                    
                    id = int(input('Qual o ID do cadastro que deseja deletar? '))
                    
                    id_exist = cursor.execute(f'SELECT * FROM agenda WHERE I_ID={id}').fetchall()
                    if len(id_exist) == 0:
                        print('\033[31mID inválido! Tente novamente!\033[m')
                        continue
                    
                    cursor.execute(f'DELETE FROM agenda WHERE I_ID={id}')
                    conn.commit()
                    
                    sleep(1)
                    print('\033[31mCadastro Deletado!\033[m')
                    sleep(1)
                
                elif op == 3:
                    if len(tabela) == 0:
                        print('>\033[34mAgenda vazia.\033[m')
                        sleep(1)
                        break
                    
                    id = int(input('Qual o ID do cadastro que deseja atualizar? '))
                    
                    id_exist = cursor.execute(f'SELECT * FROM agenda WHERE I_ID={id}').fetchall()
                    if len(id_exist) == 0:
                        print('\033[31mID inválido! Tente novamente!\033[m')
                        continue
                    
                    novo_n = str(input('Novo nome:')).strip().title()
                    novo_tel = str(input('Novo telefone: ')).strip()
                    novo_email = str(input('Novo email: ')).strip()
                    
                    cursor.execute(f'UPDATE agenda SET (T_Nome, T_Telefone, T_Email)=("{novo_n}", "{novo_tel}", "{novo_email}") WHERE I_ID={id}')
                    conn.commit()
                    
                    sleep(1)
                    print('\033[36mCadastro Atualizado!\033[m')
                    sleep(1)
                
                elif op == 4:
                    if len(tabela) == 0:
                        print('>\033[34mAgenda vazia.\033[m')
                        sleep(1)
                        break
                    
                    titulo('Agenda de Cadastros')
                    for c in tabela:
                        print(f'ID: {c[0]:<3} |Nome: {c[1]:<20} |Telefone: {c[2]:<15} |Email: {c[3]:<45}')
                        sleep(0.5)
                    
                    sleep(2)
                
                elif op == 5:
                    if len(tabela) == 0:
                        print('>\033[34mAgenda vazia.\033[m')
                        sleep(1)
                        break
                    
                    id = int(input('Qual o ID do cadastro que deseja ver? '))
                    
                    id_exist = cursor.execute(f'SELECT * FROM agenda WHERE I_ID={id}').fetchall()
                    if len(id_exist) == 0:
                        print('\033[36mID inexistente!\033[m')
                        continue
                    
                    for c in id_exist:
                        print(f'ID: {c[0]:<3} |Nome: {c[1]:<20} |Telefone: {c[2]:<15} |Email: {c[3]:<45}')
                    
                    sleep(2)
                
                else:
                    if len(tabela) == 0:
                        print('>\033[34mAgenda vazia.\033[m')
                        sleep(1)
                        break
                    
                    cons_nome = str(input('Qual o nome do cadastro que deseja ver? ')).strip().title()
                    
                    nome_exist = cursor.execute(f'SELECT * FROM agenda WHERE T_Nome="{cons_nome}"').fetchall()
                    if len(nome_exist) == 0:
                        print('\033[36mNome inexistente!\033[m')
                        continue
                    
                    for n in nome_exist:
                        print(f'ID: {n[0]:<3} |Nome: {n[1]:<20} |Telefone: {n[2]:<15} |Email: {n[3]:<45}')
                    
                    sleep(2)
            except (ValueError, TypeError, IndexError, KeyboardInterrupt):
                print('\033[31mERRO! Dado inválido!\033[m')
            else:
                break
    else:
        titulo('Saindo do Programa...')
        sleep(2)
        break

print('\033[36mPrograma Finalizado!\033[m')
cursor.close()
conn.close()
