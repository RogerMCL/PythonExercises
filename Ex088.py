# EXERCÍCIO 088:

from random import randint

print('===== JOGO MEGA-SENA =====')
n = int(input('Quantos jogos você deseja sortear?: '))
lista_num = list()

for c in range(0, n):
    for d in range(0, 6):
        num = randint(0, 60)
        lista_num.append(num)
    print(f'{c + 1}º Jogo: {lista_num}')
    lista_num.clear()
