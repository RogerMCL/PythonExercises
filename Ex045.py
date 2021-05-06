#EXERCÍCIO 045:

from random import randint

pc = randint(0, 2)

print('====== PEDRA, PAPEL OU TESOURA ======')
j = int(input('\n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA\n\nEscolha sua opção: '))

if j == 0:
    if pc == 0:
        print('\nPEDRA X PEDRA \n\nEMPATE!')
    elif pc == 1:
        print('\nPEDRA X PAPEL \n\nCOMPUTADOR VENCEU!')
    else:
        print('\nPEDRA X TESOURA \n\nVOCÊ VENCEU!')
elif j == 1:
    if pc == 0:
        print('\nPAPEL X PEDRA \n\nVOCÊ VENCEU!')
    elif pc == 1:
        print('\nPAPEL X PAPEL \n\nEMPATE!')
    else:
        print('\nPAPEL X TESOURA \n\nCOMPUTADOR VENCEU!')
elif j == 2:
    if pc == 0:
        print('\nTESOURA X PEDRA \n\nCOMPUTADOR VENCEU!')
    elif pc == 1:
        print('\nTESOURA X PAPEL \n\nVOCÊ VENCEU!')
    else:
        print('\nTESOURA X TESOURA \n\nEMPATE!')
else:
    print('\nOPÇÃO INVÁLIDA!')
