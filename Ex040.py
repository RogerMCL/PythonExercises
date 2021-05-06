#EXERCÍCIO 040:

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if 7 <= media <= 10:
    print(f'\nAPROVADO! Média: {media:.1f}')
elif 5 <= media < 7:
    print(f'\nRECUPERAÇÃO! Média: {media:.1f}')
elif 0 <= media < 5:
    print(f'\nREPROVADO! Média: {media:.1f}')
else:
    print(f'\nNOTAS INVÁLIDAS!')
