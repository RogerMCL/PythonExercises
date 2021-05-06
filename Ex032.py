#EXERCÍCIO 032:

from datetime import date
a = int(input('(Digite "0" para o ano atual) Ano: '))

if a == 0:
    a = date.today().year
    
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'\n{a} é BISSEXTO!')
else:
    print(f'\n{a} NÃO é BISSEXTO!')
