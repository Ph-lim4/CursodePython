#PA

pt = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais

    while c <= total:
        print(pt, '-> ', end='')
        pt = pt + ra
        c += 1
    mais = int(input('Quantos mais? '))
print('Total de termos: {}'.format(total))
print('FIM')