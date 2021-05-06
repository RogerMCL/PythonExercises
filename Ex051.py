#EXERCÍCIO 051:

print('==== 10 TERMOS DE UMA PA ====')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('')
for c in range(0, 10):
    print(n, end=' -> ')
    n += r
print('FIM')
