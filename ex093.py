# Jogadores
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for v in range(0, partidas):
    goljogo = int(input(f'Quantos gols na partida {v + 1}: '))
    gols.append(goljogo)
    total = total + goljogo
print('-=' * 20)
jogador['gols'] = gols[:]
jogador['total'] = total
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas!')
for n, i in enumerate(gols):
    print(f'Na partida {n + 1}, ele fez {i} gols...')
print(f'Um total de {total} gols...')
print('-=' * 20)
