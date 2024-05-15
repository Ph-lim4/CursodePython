#Somador impares multiplos de 3

soma = 0
cont = 0
for n in range(1, 501, 2):

    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n

print("Numeros", cont,"Soma", soma)
