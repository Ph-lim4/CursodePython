# Somador de pares

soma = 0
cont = 0
for c in range(1, 7):
    print('{}º Numero: '.format(c))
    num = int(input(" "))
    c = c + 1

    if num % 2 == 0:
        soma += num
        cont += 1
print('=-'*8)
print('Numeros: {} Soma: {}'.format(cont, soma))
print('=-' * 8)
