print('='*8,'Gerenciador de Pagamentos','='*8)

print('{:-^40}'.format('Loja do Seu Josefino'))
p = float(input('Preco das compras: R$'))
print('''Qual sera a condicao de pagamento?
[1] A vista dinheiro/cheque
[2] A vista no cartao
[3] Em ate 2x no cartao
[4] 3x ou mais no cartao''')
op = int(input('Opcao escolhida: '))

if op == 1:
    np = p*0.9
    print('O valor da sua compra ficara por R${:.2f}.'.format(np))
elif op == 2:
    np = p*0.95
    print('O valor da sua compra ficara por R${:.2f}.'.format(np))
elif op == 3:
    np = p
    print('O valor da sua compra em 2 parcelas ficara por R${:.2f}.'.format(np))
elif op == 4:
    pa = int(input('Em quantas parcelas? '))
    np = p*1.20
    print('O valor da sua compra em {} parcelas ficara por R${:.2f}.'.format(pa,np))
else:
    print('{}Opcao invalida!{}'.format('\033[31m','\033[m'))
