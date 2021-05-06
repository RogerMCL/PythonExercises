# EXERCÍCIO 084:

lista = list()
pessoas = list()
p_maior = p_menor = 0
while True:
    n = str(input('Nome: '))
    pessoas.append(n)
    p = float(input('Peso: '))
    pessoas.append(p)
    lista.append(pessoas[:])
    if len(lista) == 1:
        p_maior = p
        p_menor = p
    else:
        if p > p_maior:
            p_maior = p
        elif p < p_menor:
            p_menor = p
    pessoas.clear()
    op = str(input('Quer continuar [S/N]: ')).lower()
    if op == 'n':
        break
    elif op != 's':
        print('ERRO! Opção inválida!')
        break

maior_peso = list()
menor_peso = list()
for c, d in enumerate(lista):
    if p_maior == lista[c][1]:
        maior_peso.append(lista[c][0])
    elif p_menor == lista[c][1]:
        menor_peso.append(lista[c][0])

print(f'\nForam cadastradas {len(lista)} pessoas!')
print(f'O maior peso foi de {p_maior:.2f}kg e a lista de pessoas com esse peso são: {maior_peso}')
print(f'O menor peso foi de {p_menor:.2f}kg e a lista de pessoas com esse peso são: {menor_peso}')
