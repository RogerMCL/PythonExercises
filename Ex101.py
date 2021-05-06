# EXERCÍCIO 101:

from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO-VOTANTE'


ano = int(input('Em que ano que você nasceu?: '))
print(voto(ano))
