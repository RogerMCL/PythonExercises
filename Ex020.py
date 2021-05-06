#EXERCÍCIO 020:

from random import shuffle

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
l = [a1, a2, a3]

shuffle(l) #Não se pode atribuir essa função a uma variável

print(f'\nA ordem de apresentação será: \n{l}')
