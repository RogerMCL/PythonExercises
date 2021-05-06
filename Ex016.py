#EXERCÍCIO 016:
from math import trunc
n = float(input('Digite um número: '))

print(f'\nA porção inteira desse número é {trunc(n)}!')
#Outra forma sem o uso da biblioteca math:
print(f'\nA porção inteira desse número é {int(n)}!')
