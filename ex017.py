import math
# Hipotenusa

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

catO = float(input('Cateto Oposto: '))
catA = float(input('Cateto Adjacente: '))
hipo = (catO ** 2 + catA ** 2) ** (1/2)
print('Hipotenusa: {} (Normal)' .format(hipo))
hipo2 = math.hypot(catO, catA)
print('Hipotenusa: {} (Math)' .format(hipo2))
