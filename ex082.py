# Pares e impares
lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Adicione um valor: ')))
    resp = input('Deseja continuar: (S/N): ')
    if resp in 'Nn':
        break
for p, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-'*30)
print(f'Lista completa: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
print('-'*30)