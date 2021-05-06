#EXERCÍCIO 038:

a = int(input('Digite o primeiro valor inteiro: '))
b = int(input('Digite o segundo valor inteiro: '))

if a > b:
    print(f'\n{a} é maior que {b}!')
elif b > a:
    print(f'\n{b} é maior que {a}!')
else:
    print('\nOs dois valores são iguais!')
