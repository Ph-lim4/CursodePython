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


