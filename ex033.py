#maior de 3

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

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
maior = 0
if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
else:
    if n2 > n3:
        print('{} é o maior'.format(n2))
    else:
        print('{} é o maior'.format(n3))
# --------------------
if n1 < n2 and n1 < n3:
    print('{} é o menor'.format(n1))
else:
    if n2 < n3:
        print('{} é o menor'.format(n2))
    else:
        print('{} é o menor'.format(n3))
