#EXERCÍCIO 028:

from random import randint
from time import sleep

adv = int(input('Tente adivinhar um número entre 0 e 5: '))
num = randint(0, 5)

print('\nPROCESSANDO...')
sleep(3)
if adv == num:
    print(f'GANHEI! Pensei no número {num}')
else:
    print(f'PERDI! Pensei no número {num} e não no {adv}!')
