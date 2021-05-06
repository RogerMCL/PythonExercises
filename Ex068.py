#EXERCÍCIO 068:

from random import randint

while True:
    print('===== PAR OU ÍMPAR =====')
    pc = randint(0, 11)
    jog = int(input('\nDigite um número [0 a 10]: '))

    if jog < 0 or jog > 10:
        print('\nNÚMERO INVÁLIDO! Tente novamente!')
        break

    jog_pi = str(input('\nPar ou ímpar? [P/I]: ')).upper()
    if jog_pi != 'P' and jog_pi != 'I':
        print('\nOPÇÃO INVÁLIDA! Tente novamente!')
        break

    result = pc + jog
    if result % 2 == 0:
        result_pi = 'P'
        pi = 'PAR!'
    else:
        result_pi = 'I'
        pi = 'ÍMPAR!'

    print(f'\nVocê jogou {jog} e o computador jogou {pc}! A soma deu {result} e é {pi}')
    if result_pi == jog_pi:
        print('\nVOCÊ GANHOU! Jogue novamente!\n')
    else:
        print(f'\nVOCÊ PERDEU! Obrigado por jogar!')
        break
