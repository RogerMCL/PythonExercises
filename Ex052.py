#EXERCÍCIO 052:

n = int(input('Informe um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ') #31(red), 32(green), 33(yellow)
        div += 1
    else:
        print('\033[31m', end=' ') #34(blue), 35(purple), 36(cian)
    print(f'{c}', end=' ')

print(f'\n\033[mO número {n} foi divisível {div} vezes!') #Outros números ou só 'm' (branco)

if div == 2:
    print('E por isso, ele é PRIMO!')
else:
    print('E por isso, ele NÃO É PRIMO!')
