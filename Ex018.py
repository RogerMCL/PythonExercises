#EXERCÍCIO 018:

from math import sin, cos, tan, radians
ang = float(input('Informe o ângulo em graus: '))
rad = radians(ang)
print(f'\nsen({ang}) = {sin(rad):.2f}') #radians(x) - converte rad em graus
print(f'cos({ang}) = {cos(rad):.2f}')
print(f'tan({ang}) = {tan(rad):.2f}')
