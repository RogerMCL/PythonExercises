# EXERCÍCIO 093:

jog = dict()
jog['Nome'] = str(input('Jogador de vôlei: '))
jog['Total de partidas'] = int(input('Quantas partidas ele jogou?: '))
jog['Pontos'] = list()
total = 0
for c in range(0, jog['Total de partidas']):
    jog['Pontos'].append(int(input(f'\tQuantos pontos ele fez na {c + 1}ª partida: ')))
for t, p in enumerate(jog['Pontos']):
    total += jog['Pontos'][t]
print('=' * 60)
print(jog)
print('=' * 60)
for k, v in jog.items():
    print(f'{k}: {v}')
print(f'Pontuação total: {total} pontos')
print('=' * 60)
print(f'O jogador {jog["Nome"]} jogou {jog["Total de partidas"]} partidas!')
for k, v in enumerate(jog['Pontos']):
    print(f'\t==> Na {k + 1}ª partida, fez {v} pontos')
print(f'Um total de {total} pontos!')
