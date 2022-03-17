print('='*8,'Radar de Velocidade','='*8)
v = float(input('Valor da velocidade media do carro em km/h: '))
m = (v-80)*7
if v<=80:
    print('{}Tenha um bom dia e dirija com cuidado!{}'.format('\033[32m','\033[m'))
else:
    print('{}Voce escedeu o limite de 80km/h! Voce devera pagar uma multa de R${:.2f}!{}'.format('\033[31m',m,'\033[m'))
