print('='*8,'Classe Triângulo','='*8)
from module import interface

class Triangulo():
    '''Tentativa de modelar um triângulo em Python'''
    def __init__(self, la, lb, lc):
        self.la = la
        self.lb = lb
        self.lc = lc
    def perimetro(self):
        soma = self.la + self.lb + self.lc
        return soma
    def getMaiorLado(self):
        l = [self.la, self.lb, self.lc]
        cont = maiorlado =  0
        for lado in l:
            if cont == 0:
                maiorlado = lado
            else:
                if lado >= maiorlado:
                    maiorlado = lado
            cont += 1
        return maiorlado
    def area(self):
        p = self.perimetro()
        sp = p / 2
        soma = sp * (sp - t.la) * (sp - t.lb) * (sp - t.lc)
        area = soma ** (1/2)
        return area


interface.menu('Análise de Um Triângulo')
interface.titulo('Lados')

while True:
    try:
        l1 = int(input('Valor do Lado 1: '))
        l2 = int(input('Valor do Lado 2: '))
        l3 = int(input('Valor do Lado 3: '))
    except (ValueError, TypeError):
        print('\033[31mValor dado inválido!\033[m')
    except KeyboardInterrupt:
        print('\033[36mValor não fornecido!\033[m')
    else:
        t = Triangulo(l1, l2, l3)
        break

interface.titulo('Dados do Triângulo')
print(f'Os lados do seu triângulo são: {t.la}, {t.lb}, {t.lc}')

p = t.perimetro()
print(f'>>> O perímetro do triângulo vale {p}')
area = t.area()
print(f'>>> A área do triângulo vale {area:.2f}cm²')
ml = t.getMaiorLado()
print(f'>>> O maior lado do triângulo vale {ml}')
