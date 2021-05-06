# EXERCÍCIO 082:

lista = list()
lista_par = list()
lista_impar = list()

print('===== LISTA DE NÚMEROS =====')
while True:
    n = int(input('\nInforme um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    op = str(input('Quer continuar? [S/N]: ')).lower()
    if op != 's' and op != 'n':
        print('\nERRO! Tente novamente!')
        break
    else:
        if op == 'n':
            break
if op == 'n':
    lista.sort()
    print(f'\nLista: {lista}')
    print(f'Números pares: {lista_par}')
    print(f'Números ímpares: {lista_impar}')
