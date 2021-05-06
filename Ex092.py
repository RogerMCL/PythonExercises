# EXERCÍCIO 092:

from datetime import date
trab = dict()
trab['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
trab['Idade'] = date.today().year - ano_nasc
trab['CTTPS'] = int(input('Carteira de Trabalho (Digite "0" se não tiver: '))
if trab['CTTPS'] != 0:
    trab['Ano de Contratação'] = int(input('Ano de Contratação: '))
    trab['Salário'] = float(input('Salário: '))
    trab['Aposentadoria'] = (trab['Ano de Contratação'] - ano_nasc) + 50
print('\n', '=' * 10, 'CADASTRO', '=' * 10)
for k, v in trab.items():
    if k == 'Salário':
        print(f'{k}: R${v:.2f}')
    elif k == 'CTTPS' and v == 0:
        print(f'{k}: Não possui')
    else:
        print(f'{k}: {v}')
