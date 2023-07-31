#PA

pt = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
c = 1
while c != 11:
    print(pt, '-> ', end='')
    pt = pt + ra
    c += 1
print('FIM')