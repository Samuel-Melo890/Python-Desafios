import re
from module.interface import *
from os import system

system('cls')
menu('Continuação de RegEx')

t = '''It was my birthday. My boyfriend Daaaaanieeeel came to my house to take me out for 
dinner.I opened the door, and he had a big bunch of flowers and a very     
nice car. He rented the car just to take me out. I was really surprised.
<pid> Frase1 <pid> <idp> Texto1 <idp> ÃÁÉ 21231'''

# |
res = re.compile(r'was|my|to')
print(res.findall(t))

print('')
# . 
res1 = re.compile(r'b.......d')
res2 = re.compile(r'.+')
print(res1.findall(t))
print(res2.findall(t))

print('')
# []
print(re.findall(r'my', t, flags = re.IGNORECASE))
print(re.findall(r'[a-zA-Z0-9]y', t))

print('')
# \
print(re.findall(r'surprised\.', t))

print('')
# +, *, ?, {}
print(re.findall(r'Da+nie+l', t, flags = re.I))
print(re.findall(r'they*', t, flags = re.I))
print(re.findall(r'houses?', t, flags = re.I))
print(re.findall(r'Da{0,5}nie{0,4}l', t, flags = re.I))
print(re.findall(r'was [really]*', t, flags = re.I))
print(re.findall(r'<[pid]*>.*?<[pid]*>', t, flags = re.I))

print('')
# ()
tags = re.findall(r'((<[pid]*>).*?\2)', t, flags = re.I)
print(tags)

print('')
# ^, $
cpf = '''453.281.190-87
213.123.423-90'''
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))

print('')
# Flags, \w+, \W+, \d+, \D+, \s, \S, \b, \B
print(re.findall(r'\w+', t, flags = re.I))
print(re.findall(r'\W+', t, flags = re.I))
print(re.findall(r'[a-zA-Z0-9]+', t, flags = re.ASCII))

print('')
print(re.findall(r'\d+', t))
print(re.findall(r'\D+', t, flags = re.I))

print('')
print(re.findall(r'\s+', t))
print(re.findall(r'\S+', t))

print('')
print(re.findall(r'\bbi\w+', t))
print(re.findall(r'\w+e\b', t))
print(re.findall(r'\b\w{5}\b', t))
print(re.findall(r'birthday\B', t))

print('')
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf, flags = re.M))
print(re.findall(r'^i.*y$', t, flags = re.I | re.S))

