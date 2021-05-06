# EXERCÍCIO 091:

from random import randint
from time import sleep
from operator import itemgetter

dic_jog = dict()
for c in range(0, 4):
    dic_jog[f'Jogador {c + 1}'] = randint(1, 6)

for k, v in dic_jog.items():
    print(f'{k} tirou {v} no dado!')
    sleep(1)

print('\n\t', '=' * 10, 'RANKING', '=' * 10, '\n')
ranking = sorted(dic_jog.items(), key=itemgetter(1), reverse=True)
# faz uma lista e ordena de forma crescente os valores de determinado item do dict,
# nesse caso o item 1 que é a pontuação, usa-se o reverse para termos uma ordem decrescente
for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0]} que tirou {v[1]} no dado!')
