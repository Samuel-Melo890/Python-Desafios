print('='*8,'Maior e Menor da Sequência','='*8)

pmaior = 0
pmenor = 0
for pess in range(1, 6):
    p = float(input('Peso da pessoa número {} em kg: '.format(pess)))
    if pess == 1:
        pmaior = p
        pmenor = p
    else:
        if p > pmaior:
            pmaior = p
        if p < pmenor:
            pmenor = p
print('Dentre os dados informados temos que: \nO menor peso foi de {:.1f}kg\nO maior peso foi de {:.1f}kg'.format(pmenor, pmaior))
