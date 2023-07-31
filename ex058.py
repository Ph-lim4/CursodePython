#Jogo da advinhação
from random import randint

computador = randint(0, 10)
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual numero eu pensei? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...')
        elif jogador < computador:
            print('Mais...')

print('Muito bem você acertou em {} tentativas!'.format(tentativas))