#EXERCÍCIO 065:

soma = 0
qtd = 0
c = ''
while c != 'N':
    n = int(input('Informe um número: '))
    soma += n
    qtd += 1
    c = str(input('Quer continuar? [S/N]: ')).upper()
print(f'Você digitou {qtd} números e a soma entre eles é {soma}!')
