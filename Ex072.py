#EXERCÍCIO 072:

num = 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'

while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if n < 0 or n > 10:
        print('\nTente novamente.', end=' ')
    else:
        for c in num:
            if c == num[n - 1]:
                print(f'\nVocê digitou o número {c.upper()}!')
        break
