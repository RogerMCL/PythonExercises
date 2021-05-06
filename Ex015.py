#EXERCÍCIO 015:

km = float(input('Quantos km rodados? '))
d = int(input('Quantos dias alugados? '))

p = (60 * d) + (0.15 * km)
print(f'O preço a ser pago será de R${p:.2f}')
