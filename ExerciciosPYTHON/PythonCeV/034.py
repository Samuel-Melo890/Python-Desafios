print('='*8,'Aumentos Multiplos','='*8)

s = float(input('Qual o valor do salario atual do funcionario? R$'))
if s<=1250.00:
    ns = s*1.15
    print('O novo salario do funcionario devera ser de R${:.2f}.'.format(ns))
else:
    ns = s*1.10
    print('O novo salario do funcionario devera ser de R${:.2f}.'.format(ns))
