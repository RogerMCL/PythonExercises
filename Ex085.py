# EXERCÍCIO 085:

lista_num = list()
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º inteiro: '))
    lista_num.append(n)

lista_par = list()
lista_impar = list()

for c, d in enumerate(lista_num):
    if lista_num[c] % 2 == 0:
        lista_par.append(lista_num[c])
    else:
        lista_impar.append(lista_num[c])

print(f'\nLista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')
