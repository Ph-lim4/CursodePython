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


def leiaint():
    while True:
        try:
            numint = int(input('Digite um numero INTEIRO: '))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'{cores["bordavermelha"]} ERRO! Digite um valor válido!{cores["limpa"]}')
        else:
            return numint
            break


def leiafloat():
    while True:
        try:
            numfloat = float(input('Digite um numero REAL: '))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'{cores["bordavermelha"]} ERRO! Digite um valor válido!{cores["limpa"]}')
        else:
            return numfloat
            break


numint = leiaint()
numfloat = leiafloat()
print(f'O número Inteiro foi: {numint}\ne o Real: {numfloat}')
