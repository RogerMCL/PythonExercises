#EXERCÍCIO 073:

robits = 'Spyro 4', 'Sling', 'Kaius 9', 'Lux Lux', 'Myron 5', 'Bemol Bits', \
         'Golbit', 'Bisbit', 'Tork', 'Brubit', 'Tractor', 'Pixbit', \
         'Flex', 'Dart', 'Fixor', 'Aquabit', 'Reboc', 'Scorp', 'Liquor', 'Grux'

print(f'A lista de Robits é:\n{robits}')
print(f'\nOs primeiros Robits são:\n{robits[:5]}')
print(f'\nOs últimos 4 Robits são:\n{robits[-4:]}')
print(f'\nOs nomes dos Robits em ordem alfabética:\n{sorted(robits)}')
print(f'\nBisbit é a {robits.index("Bisbit") + 1}ª robit!') #aspas duplas
