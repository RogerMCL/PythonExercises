#EXERCÍCIO 071:

print('===== CAIXA ELETRÔNICO =====')
valor = int(input('Valor do saque: R$'))
total = valor
ced = 100
n_ced = 0

while True:
    if total >= ced:
        total -= ced
        n_ced += 1
    else:
        if n_ced > 0:
            print(f'\nTotal de {n_ced} cédulas de {ced}')

        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1

        n_ced = 0
        if total == 0:
            break
