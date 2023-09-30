# sortear e somar, na função
from random import randint


def sortear(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Numeros sorteados: ', end='')
    for n in lista:
        print(f'{n}', end=' ')

def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
    print(f'A soma dos numeros pares de {lista} é : {soma}')


numeros = list()
sortear(numeros)
print()
somapar(numeros)
