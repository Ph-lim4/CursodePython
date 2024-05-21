cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m'
}


def leiadinheiro(frase):
    valido = False
    while not valido:
        entrada = str(input(f'{frase}')).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'{cores["vermelho"]}Valor inválido! Digite um valor válido...{cores["limpa"]}')
        else:
           valido = True
           return float(entrada)


