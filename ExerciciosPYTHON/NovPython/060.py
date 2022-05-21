from module.interface import menu
from os import system

system('cls')
menu('Dictionary Comprehension')

l = ['Jeanne', 'Samuel', 'Veda', 'Astolfo', 'Pedro']

d = {k: len(k.replace(' ', '')) for k in l}
for k, v in d.items():
    print(f'\033[36m{k:.<15}\033[m\033[35m{v} letras\033[m')
