#EXERCÍCIO 066:

soma = 0
qtd = 0
while True:
    n = int(input('Informe um número [999 para parar]: '))
    if n == 999:
        break
    qtd += 1
    soma += n
print(f'\nVocê digitou {qtd} números e a soma entre eles é {soma}!')
