# Tabuada

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

n = int(input('Digite um numero para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {}' .format(n, 1, n*1))
print('{} x {:2} = {}' .format(n, 2, n*2))
print('{} x {:2} = {}' .format(n, 3, n*3))
print('{} x {:2} = {}' .format(n, 4, n*4))
print('{} x {:2} = {}' .format(n, 5, n*5))
print('{} x {:2} = {}' .format(n, 6, n*6))
print('{} x {:2} = {}' .format(n, 7, n*7))
print('{} x {:2} = {}' .format(n, 8, n*8))
print('{} x {:2} = {}' .format(n, 9, n*9))
print('{} x {} = {}' .format(n, 10, n*10))
print('-' * 12)

