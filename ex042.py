#analisando triangulos

reta01 = int(input('Reta 01: '))
reta02 = int(input('Reta 02: '))
reta03 = int(input('Reta 03: '))

if reta01 < reta02 + reta03 and reta02 < reta01 + reta03 and reta03 < reta01 + reta02:
    print('Podem formar um triângulo:', end='')
    if reta01 == reta02 == reta03:
        print(' EQUILÁTERO')
    elif reta01 != reta02 != reta03 != reta01 :
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Não podem formar um triangulo!')
