from module.interface import menu
from os import system

system('cls')
menu('Dictionary Comprehension')

l = [('nome', 'Jeanne'), ('idade', 19)]
d = {x.upper(): y*2 for x, y in l}
print(d)
