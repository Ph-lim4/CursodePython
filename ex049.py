# Calculadora 2.0
num = int(input('Digite o numero: '))

soma = 0

for c in range(1, 11):
    prod = c * num
    print('{} x {:>2} = {:>2}'.format(num, c, prod))
    c = c + 1
