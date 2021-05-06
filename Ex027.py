#EXERCÍCIO 027:

nome = str(input('Digite seu nome completo: '))
div = nome.split()

print('\nMuito prazer em te conhecer!')
print(f'Seu primeiro nome é {div[0].capitalize()}!')
print(f'Seu último nome é {div[len(div) - 1].capitalize()}!')
