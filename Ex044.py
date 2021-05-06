#EXERCÍCIO 044:

p = float(input('Preço das compras: R$'))

op = int(input('''\nFORMAS DE PAGAMENTO:
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] PARCELADO 2X CARTÃO
[ 4 ] PARCELADO 3X CARTÃO

Escolha sua opção: '''))

if op == 1:
    p = p - (p * 0.1)
    print(f'\nPagamento: R${p:.2f}')
elif op == 2:
    p = p - (p * 0.05)
    print(f'\nPagamento: R${p:.2f}')
elif op == 3:
    print(f'\nPagamento: R${p:.2f}')
elif op == 4:
    p = p + (p * 0.2)
    print(f'\nPagamento: R${p:.2f}')
else:
    print('\nOPÇÃO INVÁLIDA!')
