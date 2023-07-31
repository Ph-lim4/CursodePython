#Conversor de Bases

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

numero = int(input('Numero em base decimal: '))
base = int(input('Qual Base deseja? |1| binaria |2| octal |3| hexadecimal: '))

if (base == 1):
    print('Em {} Binario {} é: {} {} {}'
          .format(cores['bordaazul'],
                  cores['limpa'],
                  cores['bordaazul'],
                  bin(numero)[2:],
                  cores['limpa']
    ))
elif(base == 2):
    print('Em {} Octal {} é: {} {} {}'
          .format(cores['bordaamarela'],
                  cores['limpa'],
                  cores['bordaamarela'],
                  oct(numero)[2:],
                  cores['limpa']
                  ))
elif(base == 3):
    print('Em {} Hexadecimal {} é: {} {} {}'
          .format(cores['bordaverde'],
                  cores['limpa'],
                  cores['bordaverde'],
                  hex(numero)[2:],
                  cores['limpa']
                  ))
else:
    print('{} ERRO {}'.format(cores['bordavermelha'], cores['limpa']))