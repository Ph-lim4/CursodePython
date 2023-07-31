#Progressão Aritmetica

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

pri = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
decimo = pri + (10 * raz)

for c in range(pri, decimo, raz):
    print('{}'.format(c), end=' ➝ ')
    c =+ 1
print('ACABOU')