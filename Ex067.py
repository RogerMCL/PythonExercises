#EXERCÍCIO 067:

print('===== TABUADA =====')
while True:
    n = int(input('\nTabuada de que valor? [Digite um valor negativo para parar]: '))
    if n < 0:
        break
    print(f'{n} x 1 = {n}')
    print(f'{n} x 1 = {2 * n}')
    print(f'{n} x 1 = {3 * n}')
    print(f'{n} x 1 = {4 * n}')
    print(f'{n} x 1 = {5 * n}')
    print(f'{n} x 1 = {6 * n}')
    print(f'{n} x 1 = {7 * n}')
    print(f'{n} x 1 = {8 * n}')
    print(f'{n} x 1 = {9 * n}')
print('\nPrograma encerrado!')
