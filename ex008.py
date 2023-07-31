# Metros, kilometros, centimetros e etc

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

n = float(input('Digite a Distancia: '))
print('Quantidade de km {}KM' .format(n/1000))
print('Quantidade de hm {}HM' .format(n/100))
print('Quantidade de dam {}DAM' .format(n/10))
print('----------')
print('Quantidade de dm {:.0f}DM' .format(n*10))
print('Quantidade de cm {:.0f}CM' .format(n*100))
print('Quantidade de mm {:.0f}MM' .format(n*1000))
