#IMC

peso = float(input('Peso Kg: '))
altura = float(input('Peso (M): '))
imc = peso / (altura * altura)


print('Seu IMC é de: {:.2f}'.format(imc))

if imc < 16 :
    print('Magreza grave!')
elif 16 < imc < 19.9 :
    print('Magreza Leve!')
elif 20 < imc < 24.9 :
    print('Normal')
elif 25 < imc < 29.9 :
    print('Sobrepeso')
elif 30 < imc < 39.9 :
    print('Obeso')
else:
    print('Obeso Mórbido')

