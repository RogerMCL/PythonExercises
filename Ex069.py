#EXERCÍCIO 069:

qtd18 = qtdM = qtdF20 = 0
while True:
    print('\n===== CADASTRO =====\n')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\nSEXO INVÁLIDO! Tente novamente!')
        break
    else:
        if idade > 18:
            qtd18 += 1

        if sexo == 'M':
            qtdM += 1
        else:
            if idade > 20:
                qtdF20 += 1

    op = str(input('\nQuer continuar? [S/N]: ')).upper()
    if op != 'S' and op != 'N':
        print('\nOPÇÃO INVÁLIDA!')
        break
    elif op == 'N':
        break

if sexo == 'M' or sexo == 'F':
    if op == 'S' or op == 'N':
        print(f'\nTotal de pessoas maiores de idade: {qtd18}')
        print(f'Total de homens cadastrados: {qtdM}')
        print(f'Total de mulheres cadastradas maiores de 20 anos: {qtdF20}')
