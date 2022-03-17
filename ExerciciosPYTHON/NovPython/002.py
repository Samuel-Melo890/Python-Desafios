print('='*8,'Dicionário de Palavras','='*8)

d = {}
d['Fato'] = '''Acontecimento acabado; evento, ocorrência: a fiscalização das barracas \nilegais é agora um fato.
\nCoisa cuja realidade pode ser comprovada; verdade, realidade: "contra fatos não há \nargumentos".
\n[Jurídico] O que foi finalizado e não pode ser mudado nem alterado.
\nEtimologia (origem da palavra fato). A palavra fato com esses sentidos deriva do latim \n"factum", com o sentido de "feito, façanha".
\nsubstantivo masculino
\nRebanho de animais, geralmente cabras, em pequeno número.
\n[Zoologia] As entranhas dos animais; miúdos.
\nVestimenta utilizada para uma ocasião específica cujos propósitos já estão determinados: \nfato de mecânico.'''

p = str(input('Qual palavra deseja ver o significado? ')).strip().title()

cont = 0
for k, v in d.items():
    if k == p:
        print(f'\033[32m{k}\033[m => \033[33m{v}\033[m')
    else:
        cont += 1
        if cont == len(d):
            print('\033[36mA palavra desejada não se encontra no dicionário\033[m')
