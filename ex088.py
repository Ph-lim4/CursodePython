# Mega Sena
from random import randint
from time import sleep
jogos = []
numeros = []
print('-' * 40)
print(f"{'JOGO DA MEGA SENA':^40}")
print('-' * 40)
vezes = int(input('Quantos jogos quer? '))
cont = 0
while cont < vezes:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            numeros.sort()
            c += 1
        if c == 6:
            break
    jogos.append(numeros[:])
    numeros.clear()
    cont += 1
print('Os Jogos sorteados foram: ')
for c in range(0, len(jogos)):
    sleep(1)
    print(f'{c+1} = {jogos[c]}')
