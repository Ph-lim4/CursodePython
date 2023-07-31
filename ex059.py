#Menu
final = False

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
while not final:
    print('-=' * 8)
    resposta = int(input(' [ 1 ] Somar \n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos Numeros\n [ 5 ] Fechar programa\n Qual a sua opção??  '))
    print('-=' * 8)

    if resposta == 1:
        print('A soma de {} e {} é {}'.format(num1, num2, (num1 + num2)))
    elif resposta == 2:
        print('O produto ente {} e {} é {}'.format(num1, num2, (num1 * num2)))
    elif resposta == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('São iguais')
    elif resposta == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
    elif resposta == 5:
        final = True
    else:
        print('Escolha um numero valido')
