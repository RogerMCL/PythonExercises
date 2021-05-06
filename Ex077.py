#EXERCÍCIO 077:

t_palavras = 'livro', 'marcador', 'editora', 'lapiseira', \
            'caneta', 'tradutor', 'revisor'

for c in t_palavras:
    qtd_vogais = 0
    vogais = ' '
    for l in c:
        if l.lower() in 'aeiou':
            qtd_vogais += 1
            vogais += l
            vogais += ' '
    print(f'A palavra {c.upper()} tem {qtd_vogais} vogais e elas são{vogais.upper()}')

