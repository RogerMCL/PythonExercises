#EXERCÍCIO 026:

frase = str(input('Digite uma frase: '))
frase = frase.strip().upper()
print('\nAnalisando a frase...')
print(f'A letra A aparece {frase.count("A")} vezes!')
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}')
print(f'A última letra A aparece na posição {frase.rfind("A") + 1}') #rfind - dir para esq
