#EXERCÍCIO 017:

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = ((ca ** 2) + (co ** 2))**(1/2)
print(f'\nA hipotenuza terá {hip:.2f}u.m')
#Outra forma
from math import hypot
print(f'\nA hipotenuza terá {hypot(ca, co):.2f}u.m!')
