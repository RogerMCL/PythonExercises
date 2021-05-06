#EXERCÍCIO 037:

n = int(input('Digite um inteiro: '))
b = int(input('''\nEscolha uma base numérica' 
              [1] BINÁRIO
              [2] OCTAL
              [3] HEXADECIMAL
              : '''))

if b == 1:
    print(f'\n{n} convertido em binário: {bin(n)[2:]}') #Retirar o dois primeiros dígitos "0b"
elif b == 2:
    print(f'\n{n} convertido em octal: {oct(n)[2:]}') #0o
elif b == 3:
    print(f'{n} convertido em hexadecimal: {hex(n)[2:].upper()}') #0x
else:
    print('\nNÚMERO INVÁLIDO!')
