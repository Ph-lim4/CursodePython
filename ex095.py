# melhorando programa dos jogadores
jogadores = list()
jogador = dict()
gols = list()
total = c = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    total = 0
    for v in range(0, jogador['partidas']):
        goljogo = int(input(f'Quantos gols na partida {v + 1}: '))
        gols.append(goljogo)
        total = total + goljogo
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar? (S/N): '))
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'{"cod":<6}{"Nome":<10}{"Gols":<10}{"Total":<6}')
for n in jogadores:
    print(f'{c:<6}{str(n["nome"]):<10}{str(n["gols"]):<10}{str(n["total"]):<6}')
    c += 1
print('-=' * 20)
while True:
    numjogador = int(input('Mostrar dados de qual jogador (999 interrompe): '))
    if numjogador == 999:
        break
    elif numjogador > c:
        print('não encontrado...')
    else:
        print(f'O jogador {jogadores[numjogador]["nome"]} jogou {jogadores[numjogador]["partidas"]} partidas!')
        for n, i in enumerate(jogadores[numjogador]["gols"]):
            print(f'Na partida {n + 1}, ele fez {i} gols...')
        print(f'Um total de {jogador["total"]} gols...')
print('-=' * 20)
