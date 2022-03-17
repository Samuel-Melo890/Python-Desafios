print('='*8,'Produto com Desconto','='*8)
pp = float(input('Qual o preco do produto? R$'))
pd5 = pp*0.95
print('O produto, que antes custava R${:.2f}, com o novo deconto de 5%, agora custa R${:.2f}.'.format(pp,pd5))
