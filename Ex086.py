# EXERCÍCIO 086:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Digite o valor [{c + 1}][{d + 1}]: '))
        matriz[c][d] = n
print('')
for c in range(0, 3):
    for d in range(0, 3):
        print(f'[{matriz[c][d]}]', end=' ')
    print('')
