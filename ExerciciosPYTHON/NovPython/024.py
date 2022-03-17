def tabela(list):
    print(f'''    0   1   2
0 | {list[0][0]} | {list[0][1]} | {list[0][2]} |
1 | {list[1][0]} | {list[1][1]} | {list[1][2]} |
2 | {list[2][0]} | {list[2][1]} | {list[2][2]} |
''')


from os import system
from module.interface import *
import random
from time import sleep

system('cls')

print('='*8,'Jogo da Velha', '='*8)

l = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
nj = v = d = e = 0

while True:
    while True:
        system('cls')
        print('')
        tabela(l)
        
        if l[0][0] == l[0][1] == l[0][2] == 'X' or l[1][0] == l[1][1] == l[1][2] == 'X' or l[2][0] == l[2][1] == l[2][2] == 'X':
            print('\033[32mO jogador venceu! Parabéns!\033[m')
            v += 1
            break
        elif l[0][0] == l[1][0] == l[2][0] == 'X' or l[0][1] == l[1][1] == l[2][1] == 'X' or l[0][2] == l[1][2] == l[2][2] == 'X':
            print('\033[32mO jogador venceu! Parabéns!\033[m')
            v += 1
            break
        elif l[0][0] == l[1][1] == l[2][2] == 'X' or l[2][0] == l[1][1] == l[0][2] == 'X':
            print('\033[32mO jogador venceu! Parabéns!\033[m')
            v += 1
            break
        
        elif l[0][0] == l[0][1] == l[0][2] == 'O' or l[1][0] == l[1][1] == l[1][2] == 'O' or l[2][0] == l[2][1] == l[2][2] == 'O':
            print('\033[31mO jogador perdeu! Que pena!\033[m')
            d += 1
            break
        elif l[0][0] == l[1][0] == l[2][0] == 'O' or l[0][1] == l[1][1] == l[2][1] == 'O' or l[0][2] == l[1][2] == l[2][2] == 'O':
            print('\033[31mO jogador perdeu! Que pena!\033[m')
            d += 1
            break
        elif l[0][0] == l[1][1] == l[2][2] == 'O' or l[2][0] == l[1][1] == l[0][2] == 'O':
            print('\033[31mO jogador perdeu! Que pena!\033[m')
            d += 1
            break
        
        else:
            if nj == 9:
                print('\033[36mDeu velha! Empate!\033[m')
                e += 1
                break
        
        try:
            sleep(1)
            print('')
            titulo('Escolha a posição')
            
            while True:
                jl = int(input('Qual linha deseja escolher? '))
                
                if jl < 0 or jl > 2:
                    print('\033[31mPreencha os dados corretamente!\033[m')
                    continue
                
                jc = int(input('Qual coluna deseja escolher? '))
                
                if jc < 0 or jc > 2:
                    print('\033[31mPreencha os dados corretamente!\033[m')
                    continue
                
                if l[jl][jc] in ' ':
                    l[jl][jc] = 'X'
                else:
                    print('\033[31mLocal inválido!\033[m')
                    continue
                
                nj += 1
                sleep(1)
                break
            
            if nj == 9:
                continue
            
            while True:
                cl = random.randint(0, 2)
                cc = random.randint(0, 2)
                if l[cl][cc] in ' ':
                    l[cl][cc] = 'O'
                    nj += 1
                    break
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO! Degite um número inteiro válido!\033[m')
    
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    else:
        nj = 0
        l[0][0] = l[0][1] = l[0][2] = ' '
        l[1][0] = l[1][1] = l[1][2] = ' '
        l[2][0] = l[2][1] = l[2][2] = ' '

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
print(f'\033[35mVitórias:\033[m {v}\n\033[35mDerrotas:\033[m {d}\n\033[35mEmpates:\033[m  {e}\n\033[32mVolte sempre!\033[m')
