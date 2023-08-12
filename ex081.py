# Extraindo dados de uma Lista
lista = []

while True:
    lista.append(int(input('Deseja adicionar um número: ')))
    resp = input('Deseja continuar: (S/N): ')
    if resp in 'Nn':
        break
print(lista)
print(f'Você digitou {len(lista)} Números!')
lista.sort(reverse=True)
print(f'Os valores em forma decrescente são: |{lista}|')

if 5 in lista:
    print('O valor 5 faz parte da Lista')
else:
    print('O valor 5 não faz parte da lista')
