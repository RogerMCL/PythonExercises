#EXERCÍCIO 059:

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
op = 0
while op != 6:
    op = int(input('\nOPÇÕES:'
                   '\n[1] somar'
                   '\n[2] subtrair'
                   '\n[3] multiplicar'
                   '\n[4] dividir'
                   '\n[5] novos números'
                   '\n[6] sair do programa'
                   '\nDigite sua opção: '))

    if op == 1:
        print(f'\n{n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'\n{n1} - {n2} = {n1 - n2}')
    elif op == 3:
        print(f'\n{n1} x {n2} = {n1 * n2}')
    elif op == 4:
        print(f'\n{n1} / {n2} = {n1 / n2}')
    elif op == 5:
        print('\nInforme novos valores: ')
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
    elif op == 6:
        print('\nPrograma terminado com sucesso!')
    else:
        if 0 <= op < 6:
            print('\nInforme uma nova opção: ')
        else:
            print('\nNÚMERO INVÁLIDO!')
