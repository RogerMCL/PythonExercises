# EXERCÍCIO 099:

from time import sleep


def maior(*n):
    m = 0
    q = 0
    print('Lista de números:', end=' ')
    for c in n:
        print(f'{c}', end=' ')
        sleep(0.5)
        if c > m:
            m = c
        q += 1
    print(f'\nForam informados {q} números e o maior deles é {m}!')
    print('-' * 60)


maior(3, 2, 4, 5)
maior(8, 5)
maior(1, 2, 3, 7, 8, 9, 4)
