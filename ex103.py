# Jogador e gols (opcionais)

def jogador(jogador='<desconhecido>', gols=None):
    print(f'O Jogador {jogador} fez {gols} gols!')



njogador = str(input('Jogador: '))
ngols = str(input('Gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if njogador.strip() == '':
    jogador(gols=ngols)
else:
    jogador(jogador=njogador, gols=ngols)


