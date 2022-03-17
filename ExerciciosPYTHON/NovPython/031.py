import re
from module.interface import *
from os import system
from time import sleep

system('cls')
menu('Caçando Palavras em Python')

txt = '''I had a great weekend. My wife and I got married 30 years ago. 
My wife and I were really surprised when our son came to our house on 
Thursday evening. He then took us to the airport and gave us two tickets 
to go to Rome! He paid for everything: the flight, the hotel, everything. 
We had a lovely weekend. We remembered the night we got married. 
It was wonderful.'''

print('')
print(txt)

while True:
    try:
        print('')
        word = str(input('Que palavra ou letra você deseja pesquisar no texto acima? ')).strip()
        if len(word) == 0:
            print('\033[31mPor favor digite ao menos uma letra para a pesquisa.\033[m')
            sleep(0.5)
            continue
        
        sleep(1)
        ocorr = len(re.findall(word.lower(), txt.lower()))
        print(f'A sequência de caracteres \033[36m"{word}"\033[m aparece \033[35m{ocorr} vezes\033[m no texto!')
        
        res = ' '
        while res not in 'SN':
            res = str(input('Quer continuar a procurar letras e palavras? [S/N] ')).strip().upper()[0]
        if res in 'N':
            break
    except:
        print('\033[31mERRO! Por favor tente novamente.\033[m')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
