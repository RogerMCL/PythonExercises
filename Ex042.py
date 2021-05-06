#EXERCÍCIO 042:

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('\nEsses lados FORMAM um triângulo EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('\nEsses lados FORMAM um triângulo ISÓSCELES!')
    else:
        print('\nEsses lados FORMAM um triãngulo ESCALENO!')
else:
    print('\nEsses lados NÃO FORMAM um triângulo!')
