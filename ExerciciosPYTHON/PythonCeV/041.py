print('='*8,'Classificando Atletas','='*8)

from datetime import date
aat = date.today().year
an = int(input('Qual o seu ano de nascimento? '))
idade = aat - an
print('Voce possui {} anos.'.format(idade))
if idade <= 9:
    print('Voce ainda e uma atleta Mirim.')
elif 9 < idade <= 14:
    print('Voce e um atleta Infantil.')
elif 14 < idade <= 19:
    print('Voce e um atleta Junior.')
elif 19 < idade <= 25:
    print('Voce ja e uma atleta Senior.')
else:
    print('Voce agora e uma atleta Master! Parabens!')
