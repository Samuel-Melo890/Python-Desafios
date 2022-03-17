print('='*8,'Aluguel de Um Carro','='*8)
d = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados com o carro?'))
pa = 60*d + 0.15*km
print('''O valor do aluguel a ser pago por este carro com {} dias alugados e {:.2f}km rodados sera de:
{}R${:.2f}{}.'''.format(d,km,'\033[32m',pa,'\033[m'))
