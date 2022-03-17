from module.interface import menu
from os import system

system('cls')
menu('Sets em Python')

s = set()

s.add(1)
s.add(2)
s.add(3)

s.update((10, 20, 30))

s.discard(2)

print(s)
print('')

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
sunion = s1 | s2 #ou s1.union(s2)
sintersect = s1 & s2 #ou s1.intersection(s2)
s1difference = s1 - s2 #ou s1.difference(s2)
s2difference = s2 - s1 #ou s2.difference(s1)
ssym_difference = s1 ^ s2 #ou s1.symmetric_difference(s2)

print(sunion)
print(sintersect)
print(s1difference)
print(s2difference)
print(ssym_difference)
