# EXERCÍCIO 097:

def title(palavra):
    print('-' * (len(palavra) + 4))
    print(f'  {palavra}')
    # 2 espaços para centralizar (metade de 4)
    print('-' * (len(palavra) + 4))


title('Curso em Vídeo Python')
