# EXERCÍCIO 100:

from random import randint
from time import sleep


def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 9)
        num.append(n)
    for d in num:
        sleep(0.5)
        print(f'{d}', end=' ')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)


num = list()
print('Sorteando 5 valores da lista: ', end='')
sorteia(num)
print('\nA soma dos valores da lista é: ', end='')
somaPar(num)
