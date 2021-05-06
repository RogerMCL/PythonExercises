#EXERCÍCIO 057:

s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if s != 'M' and s != 'F':
        print('\nDados inválidos! Digite novamente')
