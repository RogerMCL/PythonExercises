# EXERCÍCIO 095:

lista_jog = list()
jog = dict()
while True:
    print('')
    jog['Nome'] = str(input('Jogador(a) de vôlei: '))
    jog['Partidas'] = int(input('Quantas partidas ele(a) jogou?: '))
    jog['Pontos'] = list()
    total = 0
    for c in range(0, jog['Partidas']):
        jog['Pontos'].append(int(input(f'\tQuantos pontos ele fez na {c + 1}ª partida: ')))
    for t, p in enumerate(jog['Pontos']):
        total += jog['Pontos'][t]
    jog['Total'] = total
    lista_jog.append(jog.copy())
    while True:
        op = str(input('\nQuer continuar? [S/N]: ')).lower()
        if op != 's' and op != 'n':
            print('ERRO! Digite apenas S ou N!\n')
        else:
            break
    if op == 'n':
        break
print('=' * 70)
for c, v in enumerate(lista_jog):
    print(f'{"Cód":<15}', end='')
    for k in v.keys():
        print(f'{str(k):<15}', end='')
    break
print()
print('-' * 70)
for c, v in enumerate(lista_jog):
    print(f'{c:<15}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 70)
