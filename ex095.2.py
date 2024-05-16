# Repeticão do exercicio para me testar

# Jogadores
jogadores = list()
jogador = dict()
gols = list()
total = c = 0
while True:
    # Cadastrando um jogador:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for v in range(0, jogador['partidas']):
        goljogo = int(input(f'Quantos gols na partida {v + 1}: '))
        gols.append(goljogo)
        total = total + goljogo
    print('-=' * 20)
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    print(jogador)
    print('-=' * 20)
    resp = str(input('Quer continuar? (S/N)'))
    if resp in 'Nn':
        break
print(jogadores)

# Tabela de aproveitamento
print(f'{"Cod":<6}{"Nome":<10}{"Gols":<10}{"Total":<10}')
for n in jogadores:
    print(f'{c:<6}{str(n["nome"]):<10}{str(n["gols"]):<10}{str(n["total"]):<10}')
    c += 1
# Apresentando um logador especifico
while True:
    numjogador = int(input('Quer exibir os detalhes de um jogador especifico? Digite o numero dele: (999 interrompe)'))
    if numjogador == 999:
        break
    elif numjogador > c:
        print('Não encontrado.')
    else:
        print(f'O jogador {jogadores[numjogador]["nome"]} jogou {jogadores[numjogador]["partidas"]} partidas!')
        for n, i in enumerate(jogadores[numjogador]["gols"]):
            print(f'Na partida {n + 1}, ele fez {i} gols...')
        print(f'Um total de {jogadores[numjogador]["total"]} gols...')

