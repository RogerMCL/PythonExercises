#EXERCÍCIO 070:

soma = prod1000 = precoBarato = 0
nomeBarato = ''
print('===== CADASTRO DE PRODUTOS =====')
while True:
    nomeProd = str(input('\nNome do produto: '))
    precoProd = float(input('Preço do produto: R$'))
    soma += precoProd

    if precoProd > 1000:
        prod1000 += 1

    if precoBarato == 0:
        precoBarato = precoProd
        nomeBarato = nomeProd
    else:
        if precoProd < precoBarato:
            precoBarato = precoProd
            nomeBarato = nomeProd
    op = str(input('\nQuer continuar?[S/N]: ')).upper()
    if op != 'S' and op != 'N':
        print('OPÇÃO INVÁLIDA!')
        break
    elif op == 'N':
        break

if op == 'S' or op == 'N':
    print(f'\nA soma do preço total dos produtos é R${soma:.2f}')
    print(f'Temos {prod1000} produtos que custam mais que R$1000.00')
    print(f'O produto mais barato é o/a {nomeBarato} que custa R${precoBarato:.2f}')
