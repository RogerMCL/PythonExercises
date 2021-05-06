#EXERCÍCIO 050:

soma = 0
qtd = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        qtd += 1

print(f'\nA soma dos {qtd} números pares digitados é {soma}!')
