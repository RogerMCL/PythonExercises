# EXERCÍCIO 080:

l = list()

for c in range(0, 5):
    n = int(input('Informe um número: '))
    if c == 0 or n > l[-1]:  # se ele for o primeiro valor ou maior que o último
        l.append(n)
        print(f'{n} adicionado ao final da lista')
    else:
        pos = 0
        while pos <= len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                print(f'{n} adicionado ao valor {pos} da lista')
                break
            pos += 1

print(f'\n{l}')
