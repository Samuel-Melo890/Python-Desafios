import re
from module.interface import *
from os import system
from time import sleep

system('cls')
menu('Procurando Posições em Python')

txt = '''I had a really terrible weekend. My boyfriend took me out to this 
really expensive restaurant. In the middle of our dinner, he gave me a very 
beautiful ring and he asked me to marry him. I was really surprised. I said 
no. I like him, but I knew I didn't want to marry him. He was quite angry 
and sad. It was awful.'''

print('')
print(txt)

while True:
    try:
        print('')
        word = str(input('Qual palavra ou letra deseja ver a posição? ')).strip()
        if len(word) == 0:
            print('\033[34mPor favor digite ao menos uma letra para a pesquisa.\033[m')
            sleep(0.5)
            continue
        
        sleep(1)
        first_ocorr = re.search(word.lower(), txt.lower())
        pi = first_ocorr.start()
        pf = first_ocorr.end()
        print(f'A sequência de caracteres \033[36m"{txt[pi:pf]}"\033[m foi encontrada pela primeira vez na \033[35mposição {first_ocorr.start() + 1}\033[m!')
        
        res = ' '
        while res not in 'SN':
            res = str(input('Deseja continuar a procurar posições de palavras? [S/N] ')).strip().upper()[0]
        if res in 'N':
            break
    except AttributeError:
        print('\033[34mPalavra não encontrada!\033[m')
    except KeyboardInterrupt:
        print('\033[31mERRO! Por favor tente novamente.\033[m')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
