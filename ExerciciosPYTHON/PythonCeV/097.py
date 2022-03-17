print('='*8,'Um Print Especial','='*8)
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


escreva('Eae Galera!')
