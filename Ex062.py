#EXERCÍCIO 062 (UPTADE 061):

print('==== 10 TERMOS DE UMA PA ====')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('')
c = 1
t = 1
while c != 10:
    print(n, end=' -> ')
    n += r
    c += 1
print(n)
n += r
while t != 0:
    t = int(input('\nDeseja adicionar quantos termos a mais? [0 para nenhum]: '))
    if t != 0:
        c = 1
        while c != t:
            print(n, end=' -> ')
            n += r
            c += 1
        print(n)
