#seno coseno tangente
import math

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

angulo = float(input("Angulo: "))
seno = math.sin(math.radians(angulo))
cose = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O SENO de {} é {:.2f}'.format(angulo,  seno))
print('O COSENO de {} é {:.2f}'.format(angulo, cose))
print('A TANGENTE de {} é {:.2f}'.format(angulo, tang))
