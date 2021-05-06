# EXERCÍCIO 081:

lista = list()
print('===== LISTA DE NÚMEROS =====')
while True:
    n = int(input('\nInforme um valor: '))
    if lista.count(n) == 0:
        lista.append(n)
    op = str(input('Quer continuar? [S/N]: ')).lower()
    if op != 's' and op != 'n':
        print('\nERRO! Tente novamente!')
        break
    else:
        if op == 'n':
            break
if op == 'n':
    lista.sort()
    print(f'\nVocê digitou {len(lista)} valores!')
    print(f'A lista em ordem decrescente: {lista.sort(reverse=True)}')
    if 5 in lista:
        print('O valor 5 se encontra na lista!')
    else:
        print('O valor 5 NÃO se encontra na lista!')
