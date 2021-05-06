# EXERCÍCIO 096:

def area(largura, comprimento):
    area = largura * comprimento
    print(f'\nA área de um terreno {largura:.2f}x{comprimento:.2f}m é de {area:.2f}m²')


l = float(input('Largura(em m): '))
c = float(input('Comprimento(em m): '))
area(l, c)
