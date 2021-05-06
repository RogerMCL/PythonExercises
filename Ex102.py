# EXERCÍCIO 102:

def fatorial(n, show=False): #É preciso mostrar o padrão True ou False declarando um tipo booleano
    """
    -> Função que mostra o fatorial de um número
    :param n: Variável do número que você deseja saber a variável
    :param show: Variável booleana que te dá a opção de ver ou não, a conta
    :return: O fatorial da variável n
    """
    f = 1
    conta = ''
    while n != 0:
        if n != 1:
            conta += f'{n} x '
        else:
            conta += f'{n}'
        f *= n
        n -= 1
    if show:
        return conta + str(f' = {f}')
    else:
        return f


help(fatorial)
print(fatorial(5, show=True))
