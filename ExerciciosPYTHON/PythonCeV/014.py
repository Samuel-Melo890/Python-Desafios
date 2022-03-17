print('='*8,'Conversor de Temperatura','='*8)
c = float(input('Me diga a temperatura em graus Celsius:'))
f = c*1.8 + 32
k = c + 273
print('''A temperatura {} graus em Celsius convertida para Fahrenheit fica: {} graus Fahrenheit.
A mesma temperatura em Kelvin fica: {} graus Kelvin.'''.format(c,f,k))
