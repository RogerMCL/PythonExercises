#EXERCÍCIO 053:

frase = str(input('Digite uma frase ou uma palavra: ')).strip().upper()
#strip - tirar os espaços desnecessários esq/dir
'''frase = frase.split() #split - divide as palavras da frase em uma lista
frase = ''.join(frase) #junta todas as palavras'''
frase = frase.replace(' ', '') #replace - troca um caractere por outro ou o anula
#print(frase)
#print(frase[::-1]) - frase invertida
inv = frase[::-1]
if frase == inv:
    print('Essa frase ou palavra É UM PALÍNDROMO!')
else:
    print('Essa frase ou palavra NÃO É UM PALÍNDROMO!')
