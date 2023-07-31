#fatorial

n = int(input('Numero: '))
num = n
f = 1
print('Fatorial {}! = '.format(num), end='')
while num != 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print('O fatorial de {} é {}'.format(n, f))
