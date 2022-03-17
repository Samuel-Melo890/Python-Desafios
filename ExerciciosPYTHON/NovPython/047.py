from module.interface import menu
import os
from time import sleep

os.system('cls')
menu('Complemento de Arquivos')

caminho = input('Digite um caminho: ')
termo = input('Digite um termo: ')
cont = 0

def formata_tam(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    
    if tamanho < kilo:
        texto = 'Bytes'
    elif tamanho < mega:
        tamanho = tamanho / kilo
        texto = 'Kilobytes'
    elif tamanho < giga:
        tamanho = tamanho / mega
        texto = 'Megabytes'
    elif tamanho < tera:
        tamanho = tamanho / giga
        texto = 'Gigabytes'
    elif tamanho < peta:
        tamanho = tamanho / tera
        texto = 'Terabytes'
    else:
        tamanho = tamanho / peta
        texto = 'Pentabytes'
    
    tamanho  =  round(tamanho, 2)
    return f'{tamanho} {texto}'.replace('.', ',')

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                caminho_compl = os.path.join(raiz, arquivo)
                nome_arq, ext_arq = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_compl)
                
                print('Encontrei o arquivo!')
                print(f'Nome: {nome_arq}')
                print(f'Extensão: {ext_arq}')
                print(f'Tamanho: {formata_tam(tamanho)}')
                print(f'Caminho completo: {caminho_compl}\n')
                
                cont += 1
                sleep(1)
            except Exception as error:
                print(f'\033[31mERRO! {error}\033[m')

print('')
print(f'{cont} arquivos encontrados!')
