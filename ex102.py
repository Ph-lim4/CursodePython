# Fatorial show = true

def fatorial(num, show=False):
    """
    -> Calcular o Fatorial de um Número
    :param num: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: Resultado
    """
    fat = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')

        fat *= n
    return fat


#print(fatorial(6, show=True))
help(fatorial)
