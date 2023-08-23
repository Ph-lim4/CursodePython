#Analise de dados listas dentro de listas
dados = []
pessoas = []
pesos = []
mai = men = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    pesos.append(dados[1])
    pesos.sort()
    pessoas.append(dados[:])
    dados.clear()

    resp = input('Quer continuar? (N/S) ')
    if resp in 'Nn':
        break
print('-'*30)
print(f'Numero de pessoas: {len(pessoas)}')
print(f'O maior peso foi: {pesos[-1]}, pesos de:', end=' ')
for p in pessoas:
    if p[1] == pesos[-1]:
        print(f'{p[0]}', end=' ')
print('')
print(f'O Menor peso foi: {pesos[0]}, pesos de:', end=' ')
for p in pessoas:
    if p[1] == pesos[0]:
        print(f'{p[0]}', end=' ')
print('')
print('-'*30)
