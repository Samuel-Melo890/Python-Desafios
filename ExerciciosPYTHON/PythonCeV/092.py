print('='*8,'Cadastro de Trabalhador em Python','='*8)
from datetime import date
d = {}
d['Nome'] = str(input('Nome: ')).strip().title()
an = int(input('Ano de nascimento: '))
d['Idade'] = date.today().year - an
d['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['CTPS'] != 0:
    d['Contratação'] = int(input('Ano de Contratação: '))
    d['Salário'] = float(input('Salário: R$'))
    d['Aposentadoria'] = (d['Contratação'] + 35) - date.today().year + d['Idade']
print('-=' * 25)
print(f'''Seu nome é {d["Nome"]}
Você tem {d["Idade"]} anos
Sua CTPS tem o valor {d["CTPS"]}''')
if d['CTPS'] != 0:
    print(f'''Seu ano de contratação foi em {d["Contratação"]}
Seu salário é de R${d["Salário"]:.2f}
Sua aposentadoria será em {d["Aposentadoria"]} anos de idade''')
