from http.client import NotConnected
from module.interface import *
from os import system

system('cls')
menu('Filas em Python')

from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print('Removido', queue.popleft())
print('Removido', queue.popleft())
print('Removido', queue.popleft())

print('For inútil')
for item in queue:
    print(item)
