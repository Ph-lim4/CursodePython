#somando numeros
c = 0
breaq = False
num = int(input('Digite um numero [999 para parar]: '))
soma = 0
while breaq != True:
    if num == 999:
        print('Você digitou {} numeros e a soma foi {}'.format(c, soma))
        breaq = True
    else:
        soma += num
        num = int(input('Digite um numero [999 para parar]: '))
    c += 1