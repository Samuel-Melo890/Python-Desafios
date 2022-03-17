from module.interface import menu
from os import system

system('cls')
menu('Trocando Valor Entre Variáveis')

x = 'Jeanne'
y = 19
z = 'Orleans'

x, y, z = y, z, x

print(x, y, z)
