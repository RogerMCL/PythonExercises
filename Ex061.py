#EXERCÍCIO 061 (UPDATE 051):

print('==== 10 TERMOS DE UMA PA ====')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('')
c = 1
while c != 10:
    print(n, end=' -> ')
    n += r
    c += 1
print(n)

'''for c in range(0, 10):
    print(n, end=' -> ')
    n += r
print('FIM')'''