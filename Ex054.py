#EXERCÍCIO 054:

from datetime import date
n = int(input('Quantas pessoas você quer cadastrar?: '))
y = date.today().year
print('')
maior = 0
menor = 0
for c in range(1, n + 1):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu?: '))
    if y - nasc >= 18:
        maior += 1
    else:
        menor += 1

print(f'\nForam cadastradas {maior} maiores de idade!')
print(f'Foram cadastradas {menor} menores de idade!')
