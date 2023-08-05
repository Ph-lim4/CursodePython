# maior e menores valores em uma tupla
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1 ,10), randint(1, 10), randint(1, 10))
print(f'Os sorteados foram: ', end='')
for c in numeros:
    print(f'{c}', end=' ')
print(f'\nO maior valor Sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
