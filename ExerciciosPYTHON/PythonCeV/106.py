print('='*8,'Sistema Interativo de Ajuda em Python','='*8)
t = '\033[1;36;44m'
b = '\033[7m'
f = '\033[m'
cores = [t, b, f]

def pyhelp(com):
    print(f'{b}')
    help(com)
    print(f'{f}')


def tit(s):
    print(f'{t}{"~"}{f}' * (len(s) + 6))
    print(f'{t}   {s}   {f}')
    print(f'{t}{"~"}{f}' * (len(s) + 6))


while True:
    from time import sleep
    tit('Programa de Ajuda PyHelp')
    com = str(input('Digite o comando ou biblioteca que deseja ver o manual: [999 para] ')).strip().lower()
    if com in '999':
        break
    tit(f'Acessando o manual do Comando {com}...')
    sleep(2)
    pyhelp(com)

print('\033[36mPrograma Finalizado!\033[m')
