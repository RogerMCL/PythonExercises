#EXERCÍCIO 036:

v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantidade de anos: '))

prest = v / (a * 12)
print(f'\nPrestação mensal: R${prest:.2f}')
if prest > (s * 0.3):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
