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


def leiaint(frase='Digite um numero INTEIRO: '):
    while True:
        try:
            numint = int(input(f'{frase}'))
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'{cores["bordavermelha"]} ERRO! Digite um valor válido!{cores["limpa"]}')
        else:
            return numint
            break

def linha():
    print('=' * 40)


def cabeçalho(frase='Menu Inicial'):
    linha()
    print(f'{frase:^41}')
    linha()


def menu():
    cabeçalho('Menu Inicial')

    print(f'{cores["amarelo"]}1{cores["limpa"]} - {cores["azul"]}Ver pessoas cadastradas{cores["limpa"]}')
    print(f'{cores["amarelo"]}2{cores["limpa"]} - {cores["azul"]}Cadastrar novas pessoas{cores["limpa"]}')
    print(f'{cores["amarelo"]}3{cores["limpa"]} - {cores["azul"]}Sair do sistema{cores["limpa"]}')
    linha()
    while True:
        alternativa = leiaint(f'{cores["verde"]}Sua Opção: {cores["limpa"]}')
        if alternativa in (1, 2, 3):
            break
        else:
            print(f'{cores["vermelho"]}ERRO! Digite uma alternativa válida...{cores["limpa"]}')
    return alternativa

