# Analise de dados de uma tupla

num1 = int(input('1) Digite um numero: '))
num2 = int(input('2) Digite outro numero: '))
num3 = int(input('3) Digite mais um numero: '))
num4 = int(input('4) Digite o ultimo numero: '))

# num = (int(input('Digite um numero: ')),
#        int(input('Digite um numero: ')),
#        int(input('Digite um numero: ')),
#        int(input('Digite um numero: '))
num = (num1, num2, num3, num4)
print('-'*30)
print(f'Numeros digitados: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na posição {num.index(3)+1}ª')
else:
    print('O valor 3 Não foi digitado!')
print(f'Os números pares foram: ', end='')
hapares = False
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        hapares = True
if hapares == False:
    print('Nenhum', end='')
print('\n','-'*30)



