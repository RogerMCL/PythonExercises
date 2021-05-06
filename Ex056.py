#EXERCÍCIO 056:

soma = 0
nM_velho = ''
somaF_20 = 0
iM_velho = 0

for c in range(1, 5):
    p = str(input(f'Nome da pessoa {c}: '))
    i = int(input(f'Idade da pessoa {c}: '))
    s = str(input(f'Sexo da pessoa {c}: '))
    print('')
    soma += i
    if s == 'M' or s == 'm':
        if i > iM_velho:
            nM_velho = p
            iM_velho = i
    elif s == 'F' or s == 'f':
        if i < 20:
            somaF_20 += 1

media = soma / 4

print(f'\nA média de idade das quatro pessoas é {media}')
print(f'O nome do homem mais velho é {nM_velho} e ele tem {iM_velho} anos!')
print(f'Existem {somaF_20} mulheres com menos de 20 anos!')
