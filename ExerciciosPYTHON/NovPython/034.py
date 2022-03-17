import re
from module.interface import *
from os import system
from time import sleep

system('cls')
menu('Substituindo Palavras no Python')

txt = '''It was my birthday. My boyfriend Daniel came to my house 
to take me out for dinner. I opened the door, and he had a big 
bunch of flowers and a very nice car. He rented the car just to 
take me out. I was really surprised.'''

print('')
print(txt)

while True:
    try:
        print('')
        
        word = str(input('Qual palavra ou letra deseja substituir no texto? ')).strip()
        if len(word) == 0:
            print('\033[34mPor favo insira ao menos uma letra.\033[m')
            sleep(0.5)
            continue
        
        new_word = str(input('Qual a nova palavra a ser posta no lugar? ')).strip()
        if len(new_word) == 0:
            print('\033[34mPor favor insira ao menos uma letra.\033[m')
            sleep(0.5)
            continue
        
        new_word = f'\033[36m{new_word}\033[m'
        novo_txt = re.sub(word, new_word, txt)
        
        sleep(2)
        print('')
        print('O novo texto fica:')
        print('')
        print(novo_txt)
        
        res = ' '
        while res not in 'SN':
            res = str(input('Deseja continuar substituindo palavras? [S/N] ')).strip().upper()[0]
        if res in 'N':
            break
    except:
        print('\033[31mERRO! Por favor tente de novo.\033[m')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
