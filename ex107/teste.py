import moeda

valor = float(input('Digite um valor: R$'))
print(f'A metade de {valor} é R${moeda.metade(valor)}')
print(f'O dobro é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos: R${moeda.aumentar(valor, 10)}')
print(f'Diminuindo 10%, temos: R${moeda.diminuir(valor, 10)}')
