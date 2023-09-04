# Jogo de dados
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}
ranking = ()
print('--------RESULTADO---------')
for k, v in jogo.items():
    print(f'O {k} tirou o número {v}')
    sleep(0.5)
print('---------RANKING---------')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for k, v in enumerate(ranking):
    print(f'{k+1}º = {v[0]} com {v[1]}')
