print('='*8,'Validando Expressões Matemáticas','='*8)
e = str(input('Digite uma expressão matemática qualquer que use parênteses: \n'))
l = []
for sim in e:
    if sim == '(':
        l.append('(')
    elif sim == ')':
        if len(l) > 0:
            l.pop(-1)
        else:
            l.append(')')
if len(l) != 0:
    print('\033[31mSua expressão está inválida!\033[m')
else:
    print('\033[32mSua expressão está válida!\033[m')

#pa = e.count('(')
#pf = e.count(')')
#ppa = e.index('(')
#ppf = e.index(')')
#upa = e.rindex('(')
#upf = e.rindex(')')
#if pa == pf and ppa < ppf and upf > upa:
    #print('Você digitou os parênteses corretamente!')
#else:
    #print('Você digitou os parênteses errado!')
