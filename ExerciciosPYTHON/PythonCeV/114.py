print('='*8,'Site Está Acessível?','='*8)
from urllib.error import URLError
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except (ConnectionError, URLError):
    print('\033[31mNão consegui acessar o site Pudim pois houve um erro de conexão!\033[m')
else:
    print('\033[36mSite Pudim acessado com sucesso!\033[m')
