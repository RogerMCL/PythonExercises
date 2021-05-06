# EXERCÍCIO 113:

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[031mERRO! Digite um número inteiro válido!\033[m')


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[031mERRO! Digite um número real válido!\033[m')


n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'\nVocê digitou o número inteiro {n} e o número real {r:.2f}')
