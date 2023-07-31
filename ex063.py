#fibonacci

ter = int(input('Quantos termos deseja mostrar? '))
c = 2
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while c != ter:
    t3 = t1 + t2
    print(' ->', t3, end='')
    t1 = t2
    t2 = t3
    c += 1