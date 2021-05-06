# EXERCÍCIO 105:

def notas(*n, sit=False):
    """
    -> Função que recolhe notas de alunos e as analisa
    :param n: Notas do aluno
    :param sit: Situação do aluno (Variável opcional)
    :return: Dicionário mostrando a quantidade de notas, a maior e menor nota, média e situação
    """
    # o asterisco antes do n, significa que estou passando vários valores
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'APROVADO!'
        elif 4 <= r['média'] < 7:
            r['situação'] = 'PROVA FINAL!'
        else:
            r['situação'] = 'REPROVADO!'
    return r


help(notas)
print(notas(9, 7.5, 8, sit=True))
