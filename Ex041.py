#EXERCÍCIO 041:

from datetime import date

ano_atual = date.today().year

ano_nasc = int(input('Ano de nascimento: '))

idade = ano_atual - ano_nasc

if 0 < idade <= 9:
    print('\nCategoria: MIRIM')
elif 9 < idade <= 14:
    print('\nCategoria: INFANTIL')
elif 14 < idade <= 19:
    print('\nCategoria: JÚNIOR')
elif 19 < idade <= 25:
    print('\nCategoria: SÊNIOR')
elif idade > 25:
    print('\nCategoria: MASTER')
else:
    print('\nIDADE INVÁLIDA!')
