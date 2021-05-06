# EXERCÍCIO 098:

from time import sleep


def contagem(i, f, p):
    msg = f'\nCONTAGEM DE {i} ATÉ {f} COM PASSO {p}:'
    print(msg)
    print('-' * len(msg))
    c = 0
    sleep(0.5)
    while i != f:
        print(f'{i}', end='\t')
        i += p
        c += 1
        sleep(0.5)
        if c % 9 == 0:
            print()
    print()


# main
contagem(1, 10, 1)
contagem(10, 0, -2)
print('\nAgora é com você!:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
