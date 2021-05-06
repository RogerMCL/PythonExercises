#EXERCÍCIO 063:

q = int(input('Quantos termos da sequência de Fibonacci queres imprimir: '))
ant = 0
prox = 1
c = 0

while c <= q:
    if c == 1:
        print(ant, end='')
    elif c == 2:
        print(' -> ', prox, end='')
    elif c > 2:
        n = ant + prox
        print(' -> ', n, end='')
        ant = prox
        prox = n
    c += 1
