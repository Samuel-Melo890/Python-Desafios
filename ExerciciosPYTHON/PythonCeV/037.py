print('='*8,'Conversor de Bases Numericas','='*8)

n = int(input('Digite um numero inteiro qualquer: '))
print('''Agora escolha qual sera a base de conversao para o numero:
[1] Binario
[2] Octal
[3] Hexadecimal''')
op = int(input('Opcao: '))
if op == 1:
    print('O numero {} convertido para binario fica {}.'.format(n, bin(n)[2:] ))
elif op == 2:
    print('O numero {} convertido para octal fica {}.'.format(n, oct(n)[2:] ))
elif op == 3:
    print('O numero {} convertido para hexadecimal fica {}.'.format(n, hex(n)[2:] ))
else:
    print('{}Opcao invalida!{}'.format('\033[31m','\033[m'))
