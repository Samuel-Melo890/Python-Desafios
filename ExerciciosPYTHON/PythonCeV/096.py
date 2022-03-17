print('='*8,'Função que Calcula Área','='*8)
def area(a, b):
    m = a * b
    print(f'A área do terreno {a:.1f}x{b:.1f} vale \033[36m{m:.2f}m²\033[m.')


l = float(input('Qual é a largura do terreno em metros? '))
c = float(input('Qual o comprimento do terreno em metros? '))
area(l, c)
