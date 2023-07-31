# Jogo da adivinhação
import random

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


# lista = [1, 2, 3, 4, 5]
# escolhido = random.choice(lista)

escolhido = random.randint(1, 5)
jogo = int(input('De 1 a 5, Qual numero  o robô escolheu??? '))

print('Acertou!!!' if escolhido == jogo else 'Errou')
print('O numero foi  {}'.format(escolhido))
