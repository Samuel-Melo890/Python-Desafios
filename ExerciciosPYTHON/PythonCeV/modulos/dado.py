def leiaDinheiro(s):
    while True:
        d = str(input(s)).strip().replace(',', '.')
        if d.isalpha() or d in '':
            print('\033[31mERRO! Preço Inválido!\033[m')
        else:
            d = float(d)
            break
    return d
