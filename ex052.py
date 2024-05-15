#Numeros primos

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

num = int(input('Numero: '))
vezes = int(0)

for c in range(1, num+1):
    if num % c != 0:
        print('{}{}{}'.format(cores['amarelo'],
                              c,
                              cores['limpa']),
              end=' ➝ ')


    else:
        vezes += 1
        print('{}{}{}'.format(cores['vermelho'],
                              c,
                              cores['limpa']),
              end=' ➝ '
        )
    c += c
print('\n O numero {} foi divisivel {} vezes!'.format(num, vezes))

if vezes == 2:
    print(' {} É Primo!'.format(num))
else:
    print(' {} NÃO É Primo!'.format(num))

