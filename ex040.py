#Media

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

n1 = float(input('Nota 01: '))
n2 = float(input('Nota 02: '))

media = (n1 + n2)/2

if (media >= 6):
    print('A media entre {} e {} é {}'.format(n1, n2, media))
    print('O Aluno está {} APROVADO {}'.format(cores['bordaverde'],cores['limpa']))
elif (media <= 5):
    print('A media entre {} e {} é {}'.format(n1, n2, media))
    print('O Aluno está {} REPROVADO {}'.format(cores['bordavermelha'],cores['limpa']))
else:
    print('A media entre {} e {} é {}'.format(n1, n2, media))
    print('O Aluno está em {} RECUPERAÇÃO {}'.format(cores['bordaamarela'],cores['limpa']))

