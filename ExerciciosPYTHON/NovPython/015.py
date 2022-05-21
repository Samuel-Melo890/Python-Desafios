print('='*8,'Dados Banco','='*8)
from module.interface import *
import sqlite3
from sqlite3 import Error

con = sqlite3.connect(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\Banco\Dados.sqlite')
cursor = con.cursor()

colunasA = cursor.execute('PRAGMA table_info("TabelaA")').fetchall()
print(colunasA)
colunasB = cursor.execute('PRAGMA table_info("TabelaB")').fetchall()
print(colunasB)

titulo('Tabela A')
dadosA = cursor.execute('SELECT * FROM TabelaA')
dadosA = cursor.fetchall()
for d in dadosA:
    print(f'ID: {d[0]:<3} A: {d[1]:<5} Número: {d[2]:<5}')

print('')

titulo('Tabela B')
dadosB = cursor.execute('SELECT * FROM TabelaB')
dadosB = cursor.fetchall()
for d in dadosB:
    print(f'ID: {d[0]:<3} B: {d[1]:<5} Código: {d[2]:<5}')

print(f'\nNúmero de linhas da tabela A e B respectivamente: {len(dadosA)} e {len(dadosB)}')
