#analisador de textos

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

nome = str(input('Qual seu nome completo? ')).strip()
print('Em maiusculo: {}'.format(nome.upper()))
print('Em minusculo: {}'.format(nome.lower()))
print('Numero de letras {}'.format(len(nome)-nome.count(' ')))
lista = nome.split()
print('Primeiro nome: {} tem {} letras '.format(lista[0], len(lista[0])))
