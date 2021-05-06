#EXERCÍCIO 029:

v = float(input('Velocidade: '))

if v > 80:
    multa = (v - 80) * 7
    print(f'\nVOCÊ FOI MULTADO!\nPreço da multa: R${multa:.2f}')
print('Dirija com segurança!')