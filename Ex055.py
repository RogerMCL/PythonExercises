#EXERCÍCIO 055:

maior = 0
menor = 0
for c in range(1, 4):
    p = float(input(f'Peso {c} em kg: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p

print(f'\nMaior peso: {maior}kg\nMenor peso: {menor}kg')
