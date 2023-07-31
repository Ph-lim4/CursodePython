#maior e menor

num = int(input('Digite um numero: '))
final = True
c = 0
soma = 0
maior = num
menor = num
while final != False:
    c += 1
    soma += num
    media = soma/c
    resp = input('Quer continuar?[S/N] ')
    if resp in 'Nn':
        final = False
    else:
        num = int(input('Digite um numero: '))

    if num <= menor:
        menor = num
    elif num >= maior:
        maior = num

print('Você digitou {} numeros, media de {}'.format(c, media))
print('Maior: {} ... Menor: {}'.format(maior, menor))