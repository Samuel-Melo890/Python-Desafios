print('='*8,'Nome','='*8)
nome = input('Diga-me seu nome:')
print('''Ola {}{}{}, e um enorme prazer te conhecer!
{}Seja bem-vindo!{}'''.format('\033[4;36m',nome,'\033[m','\033[32m','\033[m'))
