#EXERCÍCIO 019:

from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
l = [a1, a2, a3] #Lista de alunos
print(f'\nO aluno escolhido foi {choice(l)}!') #Função que retorna algo de uma lista
