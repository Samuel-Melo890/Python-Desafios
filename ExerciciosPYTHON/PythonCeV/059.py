print('='*8,'Criando um Menu de Opções','='*8)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    from time import sleep
    sleep(1.5)
    print('''{}O que deseja fazer com esses números?{}
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa'''.format('\033[4;33m', '\033[m'))
    op = int(input('Qual a sua opção? '))
    sleep(0.5)
    if op == 1:
        s = n1 + n2
        print('>>>>> A soma entre os números {} e {} vale {}.'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('>>>>> A multiplicação entre os números {} e {} vale {}.'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            print('>>>>> O número {} é o maior.'.format(n1))
        elif n2 > n1:
            print('>>>>> O número {} é o maior.'.format(n2))
        else:
            print('>>>>> Os dois números são iguais.')
    elif op == 4:
        print('>>>>> Ok, me dê novos valores.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('{}Programa finalzado!{}'.format('\033[36m', '\033[m'))
    else:
        print('{}Opção inválida!{}. Tente outra vez.'.format('\033[31m', '\033[m'))
