#EXERCÍCIO 076:

t_preco = ('Caderno', 5.00, 'Lápis', 1.50, 'Borracha', 2.00, 'Transferidor', 4.50)

print('=' * 28)
print('\tLISTAGEM DE PREÇOS')
print('=' * 28)

for c, d in enumerate(t_preco):
    if c % 2 == 0:
        print(f'{d:.<20}', end=' ')
        #Será colocada a string, e no resto, '.' até completar 20 caracteres
    else:
        print(f'R${d:.2f}')

