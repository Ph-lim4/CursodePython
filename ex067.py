#Calculadora 3.0
num = 0
while True:
    num = int(input('Digite o numero: '))
    c = 1
    if num > 0:
        while c <= 10:
            prod = c * num
            print('{} x {} = {}'.format(num, c, prod))
            c = c + 1
    else:
        break
print('TABUADA FINALIZADA')