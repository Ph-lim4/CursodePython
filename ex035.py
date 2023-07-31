#pode ser triangulo??

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

n1 = float(input('Reta 01: '))
n2 = float(input('Reta 02: '))
n3 = float(input('Reta 03: '))


if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('{}Forma triangulo! {}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Não forma Triangulo! {}'.format(cores['vermelho'], cores['limpa']))