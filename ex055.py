#maior e menor

maior = 0
menor = 99999

for c in range(1, 6):
    num = int(input('Numero: '))

    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))

