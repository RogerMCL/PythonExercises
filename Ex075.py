#EXERCÍCIO 075:

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))

t = n1, n2, n3, n4

print(f'\nVocê digitou os valores: {t}')
qtd_pares = 0

if t.count(9) != 0 and t.count(9) != 1:
    print(f'O valor 9 apareceu {t.count(9)} vezes!')
elif t.count(9) == 1:
    print('O valor 9 apareceu uma vez!')
else:
    print('O valor 9 apareceu nenhuma vez!')

if 3 in t:
    print(f'O valor 3 está na {t.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez!')

for c in t:
    if c % 2 == 0:
        qtd_pares += 1
if qtd_pares != 0 and qtd_pares != 1:
    print(f'{qtd_pares} valores pares foram digitados!')
elif qtd_pares == 1:
    print('1 valor par foi digitado!')
else:
    print('Nenhum valor par foi digitado!')
