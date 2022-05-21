print('='*8,'Funcionários Banco','='*8)
from operator import itemgetter
from module.interface import *
import sqlite3
from sqlite3 import Error

con = sqlite3.connect(r'C:\Users\saymu\Documents\MyRepository\Python-Desafios\ExerciciosPYTHON\NovPython\Banco\Funcionarios.sqlite')
cursor = con.cursor()

s = 'SELECT * FROM FUNCIONARIOS'
cursor.execute(s)
fun = cursor.fetchall()
menu('Tabela de Funcionários')
for id, nome, idade, cargo, salario in fun:
    print(f'{id:<3} Nome: {nome:<15} Idade: {idade:<5} Cargo: {cargo:<15} Salário: R${salario:<8}')
print('-' * 78)

menu('Tabela em Ordem Por Salário')
funsal = cursor.execute('SELECT * FROM FUNCIONARIOS ORDER BY SALARIO ASC').fetchall()
for f in funsal:
    print(f'{f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: R${f[4]:<8}')
print('-' * 78)

print(f'\nNúmeros de linhas da tabela: {len(fun)}')
ordemsal = sorted(fun, key=itemgetter(4), reverse=True)
print('\nOs dois maiores salários foram:')
cont = 0
for f in ordemsal:
    print(f'{f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: {f[4]:<8}')
    cont += 1
    if cont == 2:
        break

sal_4000_8000 = cursor.execute('SELECT * FROM FUNCIONARIOS WHERE SALARIO BETWEEN 4000 and 8000')
print('\nSalários entre R$4000,00 e R$8000,00:')
for f in sorted(sal_4000_8000, key=itemgetter(4)):
    print(f'>> R${f[4]},00')

print('\nDados do funcionários 1 e 3:')
for f in fun:
    if f[0] == 1 or f[0] == 3:
        print(f'ID: {f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: {f[4]:<8}')

fun_id = cursor.execute('SELECT * FROM FUNCIONARIOS WHERE ID NOT IN (1,3, 5)')
print('\nDados dos funcionários com IDs diferentes de 1, 3 e 5:')
for f in fun_id:
    print(f'ID: {f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: {f[4]:<8}')

fun_nomeA = cursor.execute('SELECT * FROM FUNCIONARIOS WHERE NOME LIKE "A%"')
print('\nFuncionários cujos nomes comecem com a letra A:')
for f in fun_nomeA:
    print(f'ID: {f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: {f[4]:<8}')

fun_nomeO = cursor.execute('SELECT * FROM FUNCIONARIOS WHERE NOME LIKE "%o%"')
print('\nFuncionários cujos nomes contenham a letra O:')
for f in fun_nomeO:
    print(f'ID: {f[0]:<3} Nome: {f[1]:<15} Idade: {f[2]:<5} Cargo: {f[3]:<15} Salário: {f[4]:<8}')

cursor.close()
con.close()
