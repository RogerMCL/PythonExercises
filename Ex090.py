# EXERCÍCIO 090:

aluno = dict()

while True:
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['media'] = float(input('Média: '))
    if 10 >= aluno['media'] >= 7:
        aluno['situação'] = 'APROVADO!'
        break
    elif 7 >= aluno['media'] >= 5:
        aluno['situação'] = 'PROVA FINAL!'
        break
    elif 5 >= aluno['media'] >= 0:
        aluno['situação'] = 'REPROVADO!'
        break
    else:
        print('\nNOTA INVÁLIDA! Tente novamente\n')

print(f'\nSituação: {aluno["situação"]}')
