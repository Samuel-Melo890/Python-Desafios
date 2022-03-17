from module.interface import menu
from os import system
from time import sleep

system('cls')
menu('Price Calculation')

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    
    if tax_percentage:
        tax_percentage = value * (tax_percentage / 100)
    if discount:
        discount = value - tax_percentage
        return f'R${discount:.2f}'.replace('.', ',')
    else:
        return f'R${value:.2f}'.replace('.', ',')

p = float(input('Qual o preço do produto? R$'))
tax = float(input('Qual a taxa de desconto sobre ele? '))
sleep(1)
p_discount = calculate_price(p, tax_percentage = tax, discount = True)
print(f'O preço do produto com {tax:.0f}% de desconto é de {p_discount}!')
