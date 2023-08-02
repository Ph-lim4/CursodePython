#Numero por extenso

cont = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Catorze', 'Quize', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    extenso = ''
    if (num >= 0) and num <= 20:
        break
    else:
        print('Número errado, digite novamente')
print(f'Você digitou o número {cont[num]}')
