print('='*8,'Aumento de Salario','='*8)
s = float(input('Qual o salario do funcionario? R$'))
sa = s*1.15
print('O salario do funconario, que antes era R${:.2f}, agora passa a ser R${:.2f}, com 15% de aumento.'.format(s,sa))
