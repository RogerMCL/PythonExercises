#EXERCÍCIO 064:

n = 0
soma = 0
q = 0
while n != 999:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n != 999:
        soma += n
        q += 1
print(f'Você digitou {q} números e soma entre eles é {soma}!')
