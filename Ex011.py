#EXERCÍCIO 011:

b = float(input('Largura da parede em m: '))
h = float(input('Altura da parede em m: '))
#Cada 2m² de parede, gasta-se 1L de tinta
print(f'\nÁrea da parede: {b * h}m²')
print(f'Quantidade de tinta necessária: {(b * h) / 2}L')
