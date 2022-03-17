print('='*8,'Lista de Convidados','='*8)
from module import interface
from time import sleep

lc = []
while True:
    interface.menu('Menu Principal')
    op = interface.options('Adicionar convidados', 'Ver lista de convidados', 'Sair do Programa')
    if op == 1:
        while True:
            sleep(1)
            interface.titulo('Novo Convidado')
            lc.append(str(input('Nome do convidado: ')).strip().title())
            r = ' '
            while r not in 'SN':
                r = str(input('Deseja adicionar mais convidados? [S/N] ')).strip().upper()[0]
            if r in 'N':
                sleep(1)
                break
    elif op == 2:
        sleep(2)
        if len(lc) == 0:
            print('Sem convidados adicionados ainda.')
        else:
            lc.sort()
            interface.titulo('Lista de Convidados')
            for n in lc:
                print(f'{n}')
        sleep(1)
    elif op == 3:
        interface.menu('Saindo do Programa...')
        sleep(2)
        break
print('\033[34mPrograma Finalizado!\033[m')
