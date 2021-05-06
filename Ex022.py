#EXERCÍCIO 022:

nome = str(input('Digite seu nome completo: '))

print('\nAnalisando seu nome...')
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem ao todo, {len(nome) - nome.count(" ")} letras!') #Tirando os espaços
lista_nome = nome.split()
#print(f'Seu primeiro nome é {lista_nome[0]} e ele tem {nome.find(" ")} letras!')
print(f'Seu primeiro nome é {lista_nome[0]} e ele tem {len(lista_nome[0])} letras!')
