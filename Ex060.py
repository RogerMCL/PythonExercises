#EXERCÍCIO 060:

n = int(input('Informe o fatorial: '))
f = n
print('')
while n != 1:
    print(f'{n} x', end=' ')
    n -= 1
    f *= n
print(f'1 = {f}')
