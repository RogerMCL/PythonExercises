#EXERCÍCIO 078:

n = list()

for c in range(0, 6):
    n.append(int(input(f'Informe um valor na posição {c}: ')))
maior = max(n)
menor = min(n)

print(f'\nO maior valor dessa lista é {max(n)} e está na(s) posição(ões) ', end='')
for p, d in enumerate(n):
    if d == maior:
        print(f'{p}...', end='')
print(f'\nO maior valor dessa lista é {min(n)} e está na(s) posição(ões) ', end='')
for p, d in enumerate(n):
    if d == menor:
        print(f'{p}...', end='')
