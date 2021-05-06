#EXERCÍCIO 048:

soma = 0
qtd = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        qtd += 1

print(f'A soma de todos os {qtd} valores ímpares múltiplos de 3 entre 1 e 500 é {soma}!')
