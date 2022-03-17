from module.interface import menu
from os import system

system('cls')
menu('Operação Ternária')

alive_user = False
msg = 'Usuário Vivo.' if alive_user else 'Usuário Morto.'

#if alive_user:
    #msg = 'Usuário Vivo.'
#else:
    #msg = 'Usuário Morto'

print(msg)
