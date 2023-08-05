# Caixa eletrônico
valor_saque = int(input('Digite o valor a ser sacado: R$'))

cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0

while valor_saque != 0:
    if valor_saque >= 50:
        cedulas_50 = valor_saque // 50
        valor_saque %= 50
    elif valor_saque >= 20:
        cedulas_20 = valor_saque // 20
        valor_saque %= 20
    elif valor_saque >= 10:
        cedulas_10 = valor_saque // 10
        valor_saque %= 10
    else:
        cedulas_1 = valor_saque
        valor_saque = 0

print('Quantidade de cédulas:')
print('R$50:', cedulas_50)
print('R$20:', cedulas_20)
print('R$10:', cedulas_10)
print('R$1:', cedulas_1)