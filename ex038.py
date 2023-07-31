#Comparador

cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'lilas':'\033[35m',
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

num1 = int(input('Primeiro Numero: '))
num2 = int(input('Segundo numero: '))

if (num1 > num2):
    print('{} O Primeiro numero é maior {}'.format(cores['verde'], cores['limpa']))
elif (num1 < num2):
    print('{} O Segundo numero é maior {}'.format(cores['amarelo'], cores['limpa']))
else:
    print('{} São iguais {}'.format(cores['lilas'], cores['limpa']))

print('-------------------')