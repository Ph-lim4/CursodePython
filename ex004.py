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

n = input('{} Digite algo: {}'.format(cores['bordavermelha'], cores['limpa']))
print('Tipo Primitivo: ', type(n))
print('Só tem espaços: ', n.isspace())
print('É numero: ', n.isnumeric())
print('É alfabetico: ', n.isalpha())
print('É alfanumerico: ', n.isalnum())
print('É maiusculo:', n.isupper())
print('É minusculo:', n.islower())
print('É capitalizada:', n.istitle())
