from ex115.menu import *
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


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Hove um erro na criação do aqruivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'{cores["vermelho"]}Erro ao LER arquivo!{cores["limpa"]}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{cores["vermelho"]}Erro ao ABRIR arquivo!{cores["limpa"]}')
    else:
        try:
            a.write(f'{nome:<30}{idade:>5} anos\n')
        except:
            print(f'{cores["vermelho"]}Erro ao CRIAR Registro!{cores["limpa"]}')
        else:
            print(f'Novo Registro de {nome} adicionado.')
            a.close()