print('='*8,'Aquele Classico da Media','='*8)

nt1 = float(input('Primeira nota do aluno: '))
nt2 = float(input('Segunda nota do aluno: '))
m = (nt1 + nt2) / 2
print('Com as notas {:.1f} e {:.1f}, o aluno obteve a media de {:.1f} pontos.'.format(nt1, nt2, m))
if m < 5:
    print('O aluno foi {}REPROVADO!{}'.format('\033[31m','\033[m'))
elif 5 <= m < 7:
    print('O aluno esta de {}RECUPERACAO!{}'.format('\033[33m','\033[m'))
else:
    print('O aluno foi {}APROVADO!{}'.format('\033[32m','\033[m'))
