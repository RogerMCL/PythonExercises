#EXERCÍCIO 043:

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('\nStatus: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\nStatus: PESO NORMAL')
elif 25 <= imc < 30:
    print('\nStatus: SOBREPESO')
elif 30 <= imc < 40:
    print('\nStatus: OBESIDADE')
elif imc >= 40:
    print('\nStatus: OBESIDADE MÓRBIDA')
else:
    print('\nINFORMAÇÕES INVÁLIDAS')
