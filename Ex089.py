# EXERCÍCIO 089:

lista_alunos = list()
aluno = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append(nome)
    aluno.append(media)
    aluno.append(n1)
    aluno.append(n2)
    lista_alunos.append(aluno[:]) # [:]obrigatório, para usar a função clear e não apagar tudo
    aluno.clear()
    op = str(input('\nQuer continuar? [S/N]: ')).lower()
    if op == 'n':
        break
    elif op != 's':
        print('ERRO! Opção inválida!')
        break
print('')
if op == 'n':
    print('Nº\t\tNOME\t\tMÉDIA')
    for c, d in enumerate(lista_alunos):
        print(f'{c}\t\t{lista_alunos[c][0]}\t\t{lista_alunos[c][1]:.2f}')
    n = 0
    while True:
        n = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))
        if 0 > n or n > (len(lista_alunos) - 1) and n != 999:
            print('ERRO! Opção inválida!')
        elif n == 999:
            print('\nProcesso concluído')
            break
        else:
            print(f'Nota 1: {lista_alunos[n][2]:.2f}\tNota 2: {lista_alunos[n][3]:.2f}')
