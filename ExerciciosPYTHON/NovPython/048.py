from module.interface import *
import os
import shutil

os.system('cls')
menu('Mover, Apagar e Copiar Arquivos')

caminho = r'C:\Users\saymu\Desktop\Teste_arq'
novo_cam = r'C:\Users\saymu\Desktop\Teste_arq\Novo_arq'

for root, dirs, files in os.walk(caminho):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_cam, file)
        #shutil.move(old_file_path, new_file_path)
        shutil.copy(old_file_path, new_file_path)
        
        #os.remove(old_file_path)
