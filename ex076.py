# Preços
# Criação da Tupla
listagem = ('Biscoito', 2.5,
            'Maçã', 1.3,
            'Arroz', 1.4,
            'Macarrão', 2,
            'Suco', 0.97,
            'Frango', 6.45)
# Cabeçalho da apresentação
print('-'*36)
print(f'{"LISTAGEM DE PREÇOS":^36}')
print('-'*36)
# Listagem em si
for pos in range(0, len(listagem)):
    # Se for par (começando com a posição 0) é impresso dentro de 30 espaços, e preenchido com "."
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    # Se for impar, mais 5 espaços, e formatado com 2 casas decimais
    else:
        print(f'€{listagem[pos]:>5.2f}')
