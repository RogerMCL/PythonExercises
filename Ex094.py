# EXERCÍCIO 094:

lista_pessoas = list()
pessoa = dict()
while True:
    pessoa['Nome'] = str(input('\nNome: '))
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).lower()
        if pessoa['Sexo'] != 'm' and pessoa['Sexo'] != 'f':
            print('ERRO! Digite apenas M ou F!\n')
        else:
            break
    while True:
        op = str(input('Quer continuar? [S/N]: ')).lower()
        if op != 's' and op != 'n':
            print('ERRO! Digite apenas S ou N!\n')
        else:
            break
    lista_pessoas.append(pessoa.copy())
    if op == 'n':
        break
soma = 0
for c, v in enumerate(lista_pessoas):
    soma += lista_pessoas[c]['Idade']
media = soma / len(lista_pessoas)
maiores_media = list()
mulheres = list()
for c, v in enumerate(lista_pessoas):
    if lista_pessoas[c]['Idade'] > media:
        maiores_media.append(lista_pessoas[c])
    if lista_pessoas[c]['Sexo'] == 'f':
        mulheres.append(lista_pessoas[c]['Nome'])
print('\n', '=' * 50, '\n')
print(f'A) Ao total, temos {len(lista_pessoas)} pessoas cadastradas.')
print(f'B) A média de idade das pessoas cadastradas é de {media} anos.')
if len(mulheres) != 0:
    print(f'C) As mulheres cadastradas são: ', end='')
    for c, m in enumerate(mulheres):
        if c == len(mulheres) - 1:
            print(f'{m}.')
        elif c == len(mulheres) - 2:
            print(m, end=' e ')
        else:
            print(m, end=', ')
else:
    print('C) Nenhuma mulher foi cadastrada.')
if len(maiores_media) != 0:
    print('D) As pessoas acima da média de idade são: ')
    for c, m in enumerate(maiores_media):
        print(f'\t{maiores_media[c]["Nome"]} com {maiores_media[c]["Idade"]} anos.')
else:
    print('D) Não há pessoas maiores que a média de idade.')
print('\nPROGRAMA ENCERRADO!')
