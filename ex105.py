# medias e dicionarios


def notas(*n, sit=False):
    """
    Função para analisar notas de uma turma
    :param n: notas
    :param sit: Mostrar ou não Situação (F or T)
    :return: Analise
    """
    analise = dict()
    analise['total'] = len(n)
    analise['maior'] = max(n)
    analise['menor'] = min(n)
    analise['media'] = sum(n)/len(n)
    if sit:
        if analise['media'] >= 6:
            sit = 'Passou'
        else:
            sit = 'Não passou'
        analise['situação'] = sit
    return analise


# Programa principal
resp = notas(4.2, 7.3, 10, sit=True)
print(resp)
