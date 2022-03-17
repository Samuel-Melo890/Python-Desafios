from os import system

system('cls')

print('='*8,'Nome e Idade Lambda','='*8)

nome_idade = lambda nome, idade: print(f'\033[36m{nome}\033[m tem \033[35m{idade} anos\033[m.')

while True:
    try:
        usuario = str(input('Qual o seu nome? ')).strip().title()
        if len(usuario) == 0:
            print('\033[33mPor favor insira um nome!\033[m')
            continue
        idade = int(input('Quantos anos você possui? '))
    except Exception as erro:
        print(f'\033[31mERRO! {erro}\033[m')
    else:
        nome_idade(usuario, idade)
        break
