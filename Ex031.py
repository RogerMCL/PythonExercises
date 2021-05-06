#EXERCÍCIO 031:

d = float(input('Distância da viagem: '))

print(f'\nDistância: {d:.2f}km')
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print(f'Preço da viagem: R${p:.2f}')
