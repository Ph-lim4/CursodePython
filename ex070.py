#comprinhas

total_gasto = 0
contador_produtos_caros = 0
nome_produto_barato = ''
preco_produto_barato = 0
primeira_iteracao = True

while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: R$'))

    total_gasto += preco_produto

    if preco_produto > 1000:
        contador_produtos_caros += 1

    if primeira_iteracao or preco_produto < preco_produto_barato:
        nome_produto_barato = nome_produto
        preco_produto_barato = preco_produto
        primeira_iteracao = False

    continuar = input('Deseja continuar? (S/N) ')
    print('-'*30)
    if continuar.upper() != 'S':
        break

print('Total gasto na compra: R$', total_gasto)
print('Quantidade de produtos com valor superior a R$1000: ', contador_produtos_caros)
print('Nome do produto mais barato: ', nome_produto_barato)