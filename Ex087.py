# EXERCÍCIO 086:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_3 = 0
for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite o valor [{c + 1}][{d + 1}]: '))
        matriz[c][d] = n
        if n % 2 == 0:
            soma_par += n
        if c == 2:
            soma_3 += n

print('')
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]}]', end=' ')
    print('')

print(f'\nA soma dos números pares é {soma_par}')
print(f'A soma dos termos da terceira linha é {soma_3}')
print(f'O maior termo da segunda linha é {max(matriz[1])}')
