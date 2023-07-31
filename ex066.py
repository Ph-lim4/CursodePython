#break
c = soma = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        print('Você digitou {} numeros e a soma foi {}'.format(c, soma))
        break
    soma += num
    c += 1
