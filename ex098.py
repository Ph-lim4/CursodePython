# Contador
from time import sleep


def contador(ini, fin, pulo):
    print('-'*40)
    print(f'Contagem de {ini} até {fin}, de {pulo} em {pulo}')
    for n in range(ini, fin, pulo):
        print(n, end=' ')
        sleep(0.3)
    print('FIM')


contador(1, 11, 1)
contador(10, -1, -2)
print('-'*40)
print('Agora é sua vez: ')
i = int(input('Inicio: '))
while True:
    fb = int(input('Final: '))
    if i > fb:
        f = fb - 1
        break
    elif i < fb:
        f = fb + 1
        break
    else:
        print('Inicio e final são iguais, tente novamente...')
pb = int(input('Intervalo: '))
if i > fb:
    p = pb - (pb * 2)
else:
    p = pb
contador(i, f, p)
