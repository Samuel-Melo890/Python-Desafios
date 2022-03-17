import urllib.request
from time import sleep

page = urllib.request.urlopen(r'http://www.pudim.com.br/')
text = page.read().decode('utf8')

stretch = str(input('Write a term you want to search in the link: ')).strip()
size = len(stretch)
start_pos = text.find(stretch)
final_pos = start_pos + size

print('Searching string', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True); sleep(0.5); print('.', end='', flush=True); sleep(0.5); print('.'); sleep(0.5)

if stretch in text:
    print(f'A string \033[36m{stretch}\033[m foi encontrada no código! Sua primeira aparição foi entre os caracteres \033[35m{start_pos}\033[m e \033[35m{final_pos}\033[m.')
else:
    print('\033[33mString não encontrada!\033[m')
