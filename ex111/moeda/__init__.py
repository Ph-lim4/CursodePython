def metade(valor=0, formato=False):
    res = valor/2
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor*2
    return res if formato is False else moeda(res)


def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * taxa / 100)
    return res if not formato else moeda(res)
    # igual a: return res if formato is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    '''
    Função que formata os valores e os deixa bonitos visualmente
    :param valor: o valor a ser recebido
    :param moeda: por padrão R$, aceita outras moedas
    :return: retorna a variável fomatada
    # Nas outras funções, caso o formato for True, res passa pela função moeda antes, para ser formatado
    '''
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, desconto=0, acrescimo=0):
    print('='*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('='*30)
    print(f'Valor analisado: \t\t{moeda(valor)}')
    print(f'A metade do valor: \t\t{metade(valor, True)}')
    print(f'O dobro do valor: \t\t{dobro(valor, True)}')
    print(f'Aumentando {acrescimo}, temos: \t{aumentar(valor, acrescimo, True)}')
    print(f'Diminuindo {desconto}, temos: \t{diminuir(valor, desconto, True)}')

