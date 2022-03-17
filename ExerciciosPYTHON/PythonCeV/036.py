print('='*8,'Aprovando um Emprestimo','='*8)

vc = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salario do comprador? R$'))
a = int(input('Em quantos anos deseja pagar a casa? '))
pm = vc / (a*12)
if pm > s*0.3:
    print('{}O seu emprestimo foi negado!{} Sua prestacao mensal seria de R${:.2f}, o que excede 30% de seu salario!'.format('\033[31m','\033[m',pm))
else:
    print('{}O seu emprestimo foi aprovado!{}'.format('\033[32m','\033[m'))
