#EXERCÍCIO 039:

from datetime import date
ano_atual = date.today().year

ano_nasc = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - ano_nasc
ano_alist = ano_nasc + 18

print(f'\nQuem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}!')

if idade == 18:
    print('Você está no ano exato de seu alistamento!')
elif idade >= 18:
    print(f'Já passou {ano_atual - ano_alist} ano(s) de seu alistamento!')
    print(f'Seu alistamento deveria ter sido feito em {ano_alist}.')
else:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento!')
    print(f'Seu alistamento deverá ser feito em {ano_alist}.')
