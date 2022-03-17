import re
from module.interface import *
from os import system
from time import sleep
from random import shuffle

system('cls')
menu('Embaralhando Palavras em Python')

txt = '''I went to our house in the country with my Family. 
It's a small house in a village in the mountains. We often 
go there at the weekends and we usually go there for a few 
weeks in the summer. It was really hot when we went this 
weekend. It was 35 degrees. I was surprised because it's July. 
It's usually cold.'''

print('')
print(txt)

txt_list = re.split(' ', txt)

while True:
    try:
        print('')
        shuffle(txt_list)
        
        words = int(input('Quantas palavras embaralhadas do texto deseja ver? '))
        novo_txt = txt_list[0:words]
        frase = ' '.join(novo_txt)
        frase = frase.replace('.', ',')
        
        sleep(2)
        print('A frase embaralhada fica:')
        print(f'>>> \033[33m{frase.upper()}\033[m.')
        
        res = ' '
        while res not in 'SN':
            res = str(input('Deseja embaralhar de novo o texto? [S/N] ')).strip().upper()[0]
        if res in 'N':
            break
    except:
        print('\033[31mERRO! Por favor tente novamente.\033[m')

system('cls')
print('\033[36mPrograma Finalizado!\033[m')
