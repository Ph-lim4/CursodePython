# Colocando numeros em uma lista, em ordem, sem o metodo sort
lista = []
for cont in range(0, 5):
    num = int(input('Digite um número: '))
    # se o for o primeiro numero( posição 0) ou for maior que o ultimo:
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Maior numero, adicionado na posição final')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)