#aprovando emprestimo

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

valorcasa = float(input('Valor da casa: '))
salario = float(input('Salario: '))
anos = int(input('Anos: '))
trintaporcento = (salario * 30)/100
pretacao = valorcasa / (anos * 12)

print('{} -------------------------------------------- {}'.format(cores['azulc'], cores['limpa']))
print('Para pagar uma casa de {} {} {} em {} {} {} anos, é necessario uma parcela de {} {:.2f} {}'
      .format(cores['bordaazul'],
              valorcasa,
              cores['limpa'],
              cores['bordaazul'],
              anos,
              cores['limpa'],
              cores['bordaamarela'],
              pretacao,
              cores['limpa']
              ))
print('Sua prestação é de {} {:.2f} {}'
      .format(cores['bordaamarela'],
              trintaporcento,
              cores['limpa']))

if (trintaporcento * 12 * anos) < valorcasa:
    print('{} Compra negada {}'.format(cores['bordavermelha'], cores['limpa']))
    falta = (valorcasa/(trintaporcento * 12)) - anos
    print('Voce precisa de mais {:.2f} anos para quitar'.format(falta))
else:
    print('{} Compra aprovada {}'.format(cores['bordaverde'], cores['limpa']))
