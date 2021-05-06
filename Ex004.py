#EXERCÍCIO 004:

a = input('Digite algo: ') #retorna sempre str em função type

print(f'\nTipo primitivo: {type(a)}')
print(f'Só espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Em maiúsculas? {a.isupper()}')
print(f'Em minúsculas? {a.islower()}')
print(f'Capitalizada? {a.istitle()}')
