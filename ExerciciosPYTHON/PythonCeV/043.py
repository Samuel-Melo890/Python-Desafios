print('='*8,'Indice de Massa Corporal','='*8)

p = float(input('Qual o seu peso? (kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = p / a**2
print('O seu IMC vale {:.2f}.'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc <= 25:
    print('Voce esta com o peso ideal.')
elif imc <= 30:
    print('Voce esta com sobrepeso.')
elif imc <= 40:
    print('Voce esta obeso.')
else:
    print('Voce esta com obesidade morbida.')
