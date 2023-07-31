#par ou impar

from random import randint

while True:
    num = int(input('Numero: '))
    numpc = randint(0, 11)
    total = num + numpc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = input('Par ou impar(P/I): ').upper()
    print(f'Você jogou {num} e o Computador {numpc}')
    res = total%2
    if res == 1:
        vencedor = 'I'
    else:
        vencedor = 'P'

    if tipo == vencedor:
        print('Você ganhou!')
    else:
        print('Você perdeu')
        break

