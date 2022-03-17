from module.interface import *
from os import system

system('cls')
menu('Pilhas em Python')

class Stack():
    def __init__(self):
        self.data = []
        self.index = 0
    def append(self, n) -> None:
        self.data.append(n)
    def pop(self):
        return self.data.pop()
    def pegar(self):
        if self.data == []:
            return []
        return self.data[-1]

stack = Stack()
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

stack_copy = stack.data.copy()
while stack_copy:
    top_item = stack_copy.pop()
    print(top_item)

#for i in stack.data[::-1]:
    #print(i)
