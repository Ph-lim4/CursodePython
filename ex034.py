# aumentos multiplos

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

salario = float(input('Digite o salario que sofrerá aumento: '))
if salario <= 1250:
    salario2 = salario + (salario * 15 / 100)
    print('O salario de {} passa a ser {}!'.format(salario, salario2))
else:
    salario2 = salario + (salario * 10 / 100)
    print('O salario de {} passa a ser {}!'.format(salario, salario2))
