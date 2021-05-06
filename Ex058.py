#EXERCÍCIO 058 (completando Ex028):

from random import randint

adv = int(input('Informe um número entre 0 e 10: '))
num = randint(0, 10)

n_palpites = 1
while adv != num:
    if adv > num:
        print('Menos... Tente novamente!')
    else:
        print('Mais... Tente novamente!')
    adv = int(input('Informe mais um número entre 0 e 10: '))
    n_palpites += 1

print(f'\nVOCÊ GANHOU! Chegou no número {num} após {n_palpites} tentativas!')
