# EXERCÍCIO 104:

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        num = num.strip()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[031mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


# Programa principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')
