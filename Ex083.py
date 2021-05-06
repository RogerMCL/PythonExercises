# EXERCÍCIO 083:

exp = str(input('Digite a expressão: '))
lista = list()

for simb in exp:
    if simb == '(':
        lista.append(simb)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(simb)
            break
            # para não haver repetição de lista vazia
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
