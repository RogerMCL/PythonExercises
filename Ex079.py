# EXERCÍCIO 079:

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
    print(f'\nVocê digitou os valores: {lista}')
