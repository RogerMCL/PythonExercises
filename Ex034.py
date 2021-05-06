#EXERCÍCIO 034:

s = float(input('Digite seu salário em R$: '))

if s >= 1250:
    s = s + (s * 0.1)
else:
    s = s + (s * 0.15)

print(f'Seu novo salário é de R${s:.2f}!')
