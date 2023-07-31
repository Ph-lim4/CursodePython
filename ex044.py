#Metodo de pagamento

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'lilas:':'\033[35m',
    'azulc':'\033[36m',

    'bordabranca':'\033[1:30:40m',
    'bordavermelha': '\033[1:30:41m',
    'bordaverde': '\033[1:30:42m',
    'bordaamarela': '\033[1:30:43m',
    'bordaazul': '\033[1:30:44m',
    'bordalilas': '\033[1:30:45m',
    'bordaazulc': '\033[1:30:46m',
    'pretoebranco':'\033[7;30m',

}

valor = float(input('Qual valor da compra? '))
novovalor = int(0)
pag = int(input('Qual o método de pagamento? \n'
                '[1] À Vista Dinheiro ou Cheque \n'
                '[2] À Vista Cartão \n'
                '[3] 2x no Cartão \n'
                '[4] 3x ou mais no cartão: \n'))

if pag == 1:
    print('')
    #10% de desconto
    novovalor = valor - (valor*10/100)
    print('Valor original: {} \n'
          'Valor a pagar {} À Vista no Dinheiro ou Cheque {} \n'
          'R${}'
          .format(valor,
                cores['bordaverde'],
                cores['limpa'],
                novovalor))
elif pag == 2:
    print('')
    #5% de desconto
    novovalor = valor - (valor*5/100)
    print('Valor original: {} \n'
          'Valor a pagar {} À Vista no Cartão {} \n'
          'R${}'
          .format(valor,
                cores['bordaverde'],
                cores['limpa'],
                novovalor))
elif pag == 3:
    print('')
    #Preço normal
    print('Valor original: {} \n'
          'Valor a pagar {} 2x no cartão {} \n'
          'R${} \n'
          '2x de {}'
          .format(valor,
                cores['bordaverde'],
                cores['limpa'],
                valor,
                (valor/2)))
elif pag == 4:
    print('')
    #20% de acréscimo
    novovalor = valor + (valor*20/100)
    vezes = int(input('Quantas vezes? '))
    print('Valor original: {} \n'
          'Valor a pagar {} 3x ou mais no cartão {} \n'
          'R${} \n'
          '{} vezes de {}'
          .format(valor,
                cores['bordaverde'],
                cores['limpa'],
                novovalor,
                vezes,
                (novovalor/vezes)))
else:
    print('')